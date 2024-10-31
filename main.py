import pandas as pd
import numpy as np
import re
import streamlit as st

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def find_from(text):
    pattern = r'Zelle payment from(.*?[^()])(?=\s*\b\w*\d)'
    match = re.search(pattern, text)
    if match:
        extracted_name = match.group(1).strip()
        print(extracted_name)
        return extracted_name
    else:
        return ""

def find_to(text):
    pattern = r'Zelle payment to(.*?[^()])(?=\s*\b\w*\d)'
    match = re.search(pattern, text)
    if match:
        extracted_name = match.group(1).strip()
        print(extracted_name)
        return extracted_name
    else:
        return ""

def callback():
    st.session_state.button_clicked = True

debit_csv = st.file_uploader("Choose Debit Report CSV File")
credit_csv = st.file_uploader("Choose Credit Report CSV File")
	
if(st.button("Scout",on_click=callback) or st.session_state.button_clicked):
    if debit_csv and credit_csv is not None:
        debit_df = pd.read_csv(debit_csv,index_col=False)
        credit_df = pd.read_csv(credit_csv,index_col=False)
        money_in = debit_df["Description"].apply(find_from).unique()[1:] #0th value is blank for unknown reason
        money_out = debit_df["Description"].apply(find_to).unique()[1:]
        for outName in money_out:
            nameString = "Zelle payment to "+outName
            amount = round(sum(debit_df["Amount"][debit_df["Description"].str.contains(nameString)]),2)
            st.write(nameString, amount)
        for inName in money_in:
            nameString = "Zelle payment from "+inName
            amount = round(sum(debit_df["Amount"][debit_df["Description"].str.contains(nameString)]),2)
            st.write(nameString, amount)
        st.write("Credit Report by Category")
        st.write(credit_df.groupby("Category")["Amount"].sum())
        st.write("Debit Report by Category")
        st.write(debit_df.groupby("Type")["Amount"].sum())
        kw_search = st.text_input("Keyword Search", value=None, key=None, on_change=None, placeholder=None)
        if(st.button("Search")):
            t_credit=sum(credit_df["Amount"][credit_df["Description"].str.contains(kw_search.title())])
            u_credit=sum(credit_df["Amount"][credit_df["Description"].str.contains(kw_search.upper())])                             
            t_debit=sum(debit_df["Amount"][debit_df["Description"].str.contains(kw_search.title())])
            u_debit=sum(debit_df["Amount"][debit_df["Description"].str.contains(kw_search.upper())])
            st.write("Credit card use for ",kw_search, t_credit+u_credit)
            st.write("Debit card use for ",kw_search, t_debit+u_debit)



