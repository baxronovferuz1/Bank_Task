import pandas as pd
import sqlite3
import openpyxl
from openpyxl.chart import BarChart, Reference



def sql_query(sql):
    conn = sqlite3.connect('task.db')
    try:
        df = pd.read_sql_query(sql, conn)
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
    conn.close()
    return df

def export_to_excel(df, filename='result.xlsx'):
    df.to_excel(filename, index=False, sheet_name='Data')
    
    
    wb = openpyxl.load_workbook(filename)
    ws = wb['Data']
    
    if len(df) > 1 and len(df.columns) >= 2:  
        chart = BarChart()
        data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(df)+1)
        cats = Reference(ws, min_col=1, min_row=2, max_row=len(df)+1)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.title = "Natijalar Grafigi"
        ws.add_chart(chart, "E5")
    
    wb.save(filename)
    print(f"Excel saqlandi: {filename}")


if __name__ == "__main__":
    sql = "SELECT region, SUM(balance) FROM Clients JOIN Accounts ON Clients.id = Accounts.client_id GROUP BY region"
    df = sql_query(sql)
    export_to_excel(df)