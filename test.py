# %%
column = input('Column Name Please: ')
if 'id' in column:
    print('done')
else:
    print('not done')
# %%

yyyy = input('Year')
mm = input('Month')
dd = input('Day')
date = (f'{dd}/{mm}/{yyyy}')
print(date)
# %%
import sqlite3

from colorama.ansi import Style

conn = sqlite3.connect('DataBase.db')

print('1. Add Column')
print('2. Change column name')
ch = input("Enter the choice: ")

if ch == '1':
    tableName = input('Enter the table name: ')
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

elif ch == '2':
    while True:
        print('use 000 to exit')
        tableName = input('Enter the table name')
        if tableName == '000':
            break
        old_col = input('Enter the column name to change: ')
        new_col = input('Enter the name you want to replace: ')
        conn.execute(f"ALTER TABLE {tableName} RENAME COLUMN {old_col} TO {new_col}")
# %%
# Add data in database
import sqlite3

conn = sqlite3.connect('DataBase.db')

tableName = input('Enter the table name')


# %%
num_fields = len(conn.cursor)
field_names = [i[0] for i in conn.description]
# %%
  
conn = sqlite3.connect('DataBase.db')
conn.execute ("""\
     select ext,
        sum(size) as totalsize,
        count(*) as filecount
     from test9
    group by ext
    order by totalsize desc;
""")

while (1):
    row = conn.fetchone ()
    if row == None:
        break
    print ("%s %s %s\n" % (row[0], row[1], row[2]))

conn.close()
conn.close()      


# %%
conn = sqlite3.connect('DataBase.db')
conn.row_factory = sqlite3.Row  
 
#field = "Rotterdam"
 
sql = '''SELECT * FROM test9'''
 
cur = conn.cursor()
cur.execute('pragma table_info("test9");')    
 
rows = cur.fetchall()
for row in rows:
    print(row.items())

# %%
conn = sqlite3.connect('DataBase.db')

rows = conn.execute('pragma table_info("test9");')
tableName = input('Enter the table name')
values = []
for row in rows:
    temp = row[1]
    if row is not None:
        row = list[row[1]]
        print(type(row))
    #print(row[1])
    value = input(f'Enter the data for {row[1]}')
    print(f"""INSERT INTO {tableName} {row[1]} VALUES ({values})""")
    values.append(value)
    print(values)
        
#conn.execute(f"""INSERT INTO {tableName} ({row[1]}) VALUES ({values})""")
# %%
conn = sqlite3.connect('DataBase.db')
tableName = input('Enter the table name')
rows = conn.execute(f'pragma table_info({tableName});')
temp_row = []
values = []
for row in rows:
    print(row[1])
    temp_row.append(row[1]) 
    print(temp_row)
temp_row = tuple(temp_row)
print(type(temp_row))
print(temp_row)

rows = conn.execute(f'pragma table_info({tableName});')
for row in rows:
    value = input(f'Enter the data for {row[1]}')
    values.append(value)
values = tuple(values)
conn.close()
conn2 = sqlite3.connect('DataBase.db')
conn2.execute(f"""INSERT INTO {tableName} {temp_row} VALUES {values}""")
# %%
conn = sqlite3.connect('DataBase.db')

rows = conn.execute('pragma table_info("test9");')
tableName = input('Enter the table name')
values = []

for row in rows:
    value = input(f'Enter the data for {row[1]}')
    values.append(value)
values = tuple(values)
print(values)
# %%
import sqlite3 
  
  
# make the database connection and cursor object
connection = sqlite3.connect("CollegeData.db")
cursor = connection.cursor()
  
# create a set of queries in executescript()
# below set of queries will create and insert
# data into table
cursor.executescript(""" 
    CREATE TABLE department( deptId INTEGER,
    deptName VARCHAR(20), deptScore INTEGER); 
  
    INSERT INTO department VALUES ( 01,'IT', 850 );
    INSERT INTO department VALUES ( 02,'COMP', 840 );
    INSERT INTO department VALUES ( 03,'CIVIL', 500 );
    INSERT INTO department VALUES ( 04,'E&TC', 650 );
""")
  
# fetch the table data
print("Table data :")
cursor.execute("SELECT * FROM department") 
print(cursor.fetchall())
  
# below set of queries will update the data
# of in the table
cursor.executescript("""
    UPDATE department set deptScore = 900 where deptId = 01;
    UPDATE department set deptScore = 890 where deptId = 02;
    UPDATE department set deptScore = 660 where deptId = 03;
    UPDATE department set deptScore = 790 where deptId = 04;
""")
  
# fetch the table data after updation
print("Table data after updation :")
cursor.execute("SELECT * FROM department") 
print(cursor.fetchall())
  
# commit the changes and close the database
# connection 
connection.commit() 
connection.close()


#%%
import os

c = os.system('tree')
#print(c)
# %%
print(f"\33[(31)m"+'Added')
# %%
from colorama import Fore

print(Fore.GREEN+'Added')

# %%
import turtle

turtle.pencolor('#3e4e5e')
#print('data')
# %%
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# %%
import turtle             
my_wn = turtle.Screen()
colors = [ "red","purple","blue","green","orange","yellow"]
turtle.bgcolor('black')
#turtle.speed(2)
for i in range(30):
   turtle.pencolor(colors[i % 6])
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()
# %%
import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
# %%
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()

#Set the geometry of tkinter frame
win.geometry("1270x724")

def get_value():
   e_text=entry.get()
   Label(win, text=e_text, font= ('Century 15 bold')).pack(pady=20)
   e_text.count
   
#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)

#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= get_value)


button.pack()
win.mainloop()
# %%
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: "+inp)

# TextBox Creation
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Print",
						command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
