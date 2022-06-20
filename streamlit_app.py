#import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
#from google.oauth2 import service_account
#from googleapiclient.discovery import build
#from googleapiclient.http import HttpRequest

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1QlPTiVvfRM82snGN6LELpNkOwVI1_Mp9J9xeJe-QoaA"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"



form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    author = cols[0].text_input("Report author:")
    bug_type = cols[1].selectbox(
        "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
    )
    comment = st.text_area("Comment:")
    cols = st.columns(2)
    date = cols[0].date_input("Bug date occurrence:")
    bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Submit")


if submitted:
    add_row_to_gsheet(
        gsheet_connector,
        [[author, bug_type, comment, str(date), bug_severity]],
    )
    st.success("Thanks! Your bug was recorded.")
    st.balloons()

expander = st.expander("See all records")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(get_data(gsheet_connector))
