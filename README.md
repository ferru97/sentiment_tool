# sentiment_tool
Perform sentiment analysis on CSVs

## Requirements
- Python 3.x downloadable from [HERE](https://www.python.org/downloads/)

## How to use
- Place the CSVs to analyze in the *resources/*
- Only the first time, open the CMD in the script folder and run `pip install -r requirements.txt` to install the requirements
- To run the script, open the CMD in the script folder and run `py main.py "csv_name" "fields_list" `. The list of fields must be separated with a semicolon: `py main.py "file.csv" "field1;field2;field3" `
- The results are saved in *results/*
