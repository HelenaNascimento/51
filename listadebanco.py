from unittest import result
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port


'''
SUPATC26
HELENA\SQL2019
inf@2016
'''

srv = str(input("Nome do Servidor: "))
pwd = str (input("Senha de Acesso: "))

database = 'master'
username = 'sa'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+srv+';DATABASE='+database+';UID='+username+';PWD='+ pwd)
cursor = cnxn.cursor()
cursor1 = cnxn.cursor()
cursor2 = cnxn.cursor()
cursor3 = cnxn.cursor()

def lista():
    
    cursor.execute("select database_id from sys.databases where database_id > 4") 
    row = cursor.fetchone() 
    while row: 
        print (row[0])
        row = cursor.fetchone()
        
    cursor1.execute("select name from sys.databases where database_id > 4") 
    row1 = cursor1.fetchone() 
    for id_bd in row < 10:
        id_bd = [str(row1[0])]
        row1 = cursor1.fetchone() 
    
    cursor2.execute("use" + id_bd )
    base = cursor2.fetchone() 
    while base: 
        print (str(base))
        row = cursor.fetchone()
    
    cursor3.execute("SELECT top 1 des_versao, des_scriptextra from PARAM")
    base = cursor1.fetchone() 
    
    for base in row < 6:   
        #print(str(base[0]))
        base = cursor.fetchone()
    
    result = [row[0], base[0]]
            


lista() 

'''
def versao():
    srv1 = server
    bd = str(lista())
    snh = password
    user = username
    cnxn1 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+srv1+';DATABASE='+bd+';UID='+user+';PWD='+ snh)
    cursor1 = cnxn1.cursor()
    #cursor1.execute("use" + lista())
    cursor1.execute("SELECT top 1 des_versao, des_scriptextra from PARAM")
    row1 = cursor1.fetchone() 
    print(str(row1[0]))
    row1 = cursor1.fetchone()

print("\n") 
versao()

    
def tela():
    num = 4
        for num in lista
'''


