import sqlite3
import pandas as pd
conn=sqlite3.connect('database.db')
query= "SELECT * FROM Drink"
df = pd.read_sql_query(query,conn)
print(df)