import sqlite3
from colorama import Fore

conn = sqlite3.connect('DataBase.db')
cursor = conn.cursor()
tableName = input('Enter the table name: ')
rows = cursor.execute(f'pragma table_info({tableName});')
temp_row = []
#values = []
for row in rows:
    print(row[1])
    temp_row.append(row[1])
    print(temp_row)
temp_row = tuple(temp_row)
print(type(temp_row))
print(temp_row)

rows = cursor.execute(f'pragma table_info({tableName});')
#count = int(input('Enter How many rows you want to enter: '))
def entry():
    values = []
    for row in rows:
        value = input(f'Enter the data for {row[1]}: ')
        values.append(value)
        print(values)
    values = tuple(values)
    print(f"INSERT INTO {tableName} {temp_row} VALUES {values};")
    #conn.execute(f"INSERT INTO {tableName} {temp_row} VALUES {values};")
ch = 'y'
while True:
    if ch == 'y' or ch == 'Y':
        values = []
        for row in rows:
            value = input(f'Enter the data for {row[1]}: ')
            values.append(value)
            #print(values)
        values = tuple(values)  
        #print(f"INSERT INTO {tableName} {temp_row} VALUES {values};")
        conn.execute(f"INSERT INTO {tableName} {temp_row} VALUES {values};")
        conn.commit()
        print(Fore.GREEN+'Added')
        ch = input('Do you want another entry: ')
        rows = cursor.execute(f'pragma table_info({tableName});')
    else:
        break

conn.close()
