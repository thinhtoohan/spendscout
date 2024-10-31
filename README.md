# Spend Scout

## About

This tool is designed to provide detailed insights into personal spending habits by analyzing CSV bank statements. It leverages pandas, a powerful data analysis library in Python, to read and process the CSV files, making it easier to filter, categorize, and report financial data.

## Key Features

* Transaction Analysis: The tool parses CSV bank statements, extracting key transaction details such as amounts, dates, and descriptions. It helps categorize spending patterns by identifying where your money is going (e.g., food, transportation, entertainment).
* Peer Transaction Tracker: Using regex, the tool searches for specific names or patterns in transaction descriptions to determine which of your friends or contacts you have had the most financial transactions with. It tallies the amount of these transactions, providing an overview of your financial interactions.
* Keyword Search: Search an exact amout of money spent on entertianment or food by typing in the name of the service(e.g., Starbucks, Netflix, Amazon).

## How to Run

Install required libraries by running the following command:
```
pip install -r requirements.txt
```

Run the streamlit app via the following command:

```
streamlit run main.py
```
