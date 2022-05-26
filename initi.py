import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

SVR = str(input("Nome do Servidor: "))
BD = str(input("Informe O Banco: " ))
US = str (input("Nome do Usuário: "))
pwd = str (input("Senha de Acesso: "))

'''
SUPATC26

inf@2016
'''

server = SVR
database = BD
username = US 
password = pwd
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT top 1 des_versao, des_scriptextra from PARAM") 
row = cursor.fetchone() 
while row: 
   # print("Versão Atual do Banco é: ")
    print( " < Versão:  > " +row[0] +" < Script Extra: > " + row[1])
    
    row = cursor.fetchone()