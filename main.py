import sys
import pandas as pd
from sentiment import parse, getFields

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def main(df,columns,fname):
    new_fields = getFields()
    total = len(df.index)
    for index, row in df.iterrows():
        printProgressBar(index, total)
        content = ""
        for col in columns:
            content += " "+str(row[col])
        sentiment_out = parse(content)
        for index2, info in enumerate(sentiment_out):
            df.loc[index,new_fields[index2]] = info

    df.to_csv("results/"+fname)

if __name__ == "__main__":

    if len(sys.argv)<3:
        print("Wrong inputs")
        sys.exit()
    
    fname = sys.argv[1]
    fields = sys.argv[2].split(";")

    df = pd.read_csv("resources/"+fname, dtype=object)
    main(df, fields, fname)

    print("Done!")