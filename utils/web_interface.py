from generator import generate_sql
from sql_query_and_excel_export import sql_query,export_to_excel
import streamlit as st


st.title("Data Analyst Assistant📊")
prompt=st.text_input("Enter your question🔎:")

if st.button("Analyse"):
    sql=generate_sql(prompt)
    st.write("SQL result", sql)
    df=sql_query(sql)
    st.dataframe(df)
    export_to_excel(df)
    with open('result.xlsx', 'rb') as f:
        st.download_button("Download Excel", f, file_name='result.xlsx')
