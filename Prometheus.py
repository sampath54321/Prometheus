# %%
import sqlite3

if __name__ == '__main__':
   print('1. Local DataBase')
   print('2. Cloud DataBase')
   ch = int(input('Enter the Choice: '))
   
   if ch == 1:
       print('<**************************>')
       print('\t1. Create Table')
       print('\t2. Update Table')
       print('\t3. Add data in Database')
       print('\t4. View Database')
       print('\t5. Delete data in Database')
       print('\t6. Delete Database')
       ch = int(input('Enter the Choice: '))
# %% Create Database

conn = sqlite3.connect('DataBase.db')


def createDatabase():
    #fileName = input('Enter the New File Name: ')
    
    """ try:
        with open(fileName+'.db', 'x') as database:
            print('DataBase Created Successfully')
    except:
        fileName = input('Please Use Different name: ')
        with open(fileName+'.db', 'x') as database:
            print('DataBase Created Successfully')
            """
    tableName = input('Enter the Table name: ')
    def rename():
        global tableName
        tableName = input('Enter the Table name: ')
    
    columns = {}
    print('Column Creation')
    print('Please use "000" after all columns are entered.\n type "help" for get help')
    for i in range(1, 100):
        column = input('Column Name Please: ')
        if column == '000':
            break
        elif column == 'help':
            print("""
            Please use the following format for the datatype\n
            'integer' for numbers\n
            'varchar' for the string\n
            'float' for the decimal\n
            'date' for the date\n
            'null' for the null\n
            Others:
            Primary key type Y/N 'Y' is yes and 'N' is no \n
            length is how long is the character will the input\n
                  """)
            continue
        if column is not None:
            columnProperties = []
            prop1 = input('Column datatype: ')
            columnProperties.append(prop1)
            
            prop2 = int(input('Length: '))
            columnProperties.append(prop2)
            prop3 = input('Primary key "press enter/NOT": ')
            prop3 = prop3.replace(' ', '')
            columnProperties.append(prop3)
            prop4 = input('Do want it as null "press enter"/not: ')
            columnProperties.append(prop4)
            print(columnProperties)
            columns.update({column : columnProperties})
            for x,y in columns.items():
                #print(x, temp)
                try:
                    temp = f"{y[0]}({y[1]}) {y[2]} primary key {y[3]} NULL"
                    conn.execute(f"""create table {tableName}(
                    {x+ " " + temp});""")
                    temp = ""
                except:
                    temp = f"{y[0]}({y[1]}) {y[3]} NULL"
                    print(x, temp)
                    conn.execute(f"""alter table {tableName} add column {x} {temp};""")
                    temp = ""
        columns.clear()
createDatabase()
# %% Update DataBase
