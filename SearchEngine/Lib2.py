
#################### SQL Server#############################################

import pymssql as sql

conn = sql.connect(server='SQLGEEK-PC', 
                   database='testdb', 
                   user='sa', 
                   password = 'corei5')

query = 'Select * from Friends'

cur = conn.cursor()  

cur.execute(query)

rowset = cur.fetchall()

for row in rowset:
    print (row)

conn.close()