
from listadebanco import lista

def chama():
    cursor.execute("select name  from sys.databases where database_id = 5") 
        row = cursor.fetchone() 
        print (str(row[0]))
        row = cursor.fetchone()