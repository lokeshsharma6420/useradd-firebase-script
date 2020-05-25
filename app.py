import tkinter as tk
from tkinter import filedialog
import xlrd
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials


root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
canvas1.pack()


def getexcel():
    path = filedialog.askopenfilename()
    workbook = xlrd.open_workbook(path, "rb")                                                                                     #path of excel (xlsx )
    sheets = workbook.sheet_names()
    required_data = []
    #required_data1 = []                                                                                                           #if password is custom than include
    for sheet_name in sheets:
        sh = workbook.sheet_by_name(sheet_name)
        for rownum in range(1,sh.nrows):                                                                                           #sheet.nrows for total no. of rows
            row_valaues = sh.row_values(rownum)
            noob=int(row_valaues[0])
            required_data.append((str(noob)))
            #required_data1.append((row_valaues[1]))                                                                             #second row for password fetching if needed

    cred = credentials.Certificate("service credential file")                                                                      #credentials file link
    firebase_admin.initialize_app(cred)
    for j in range(1,sh.nrows):
        user = auth.create_user(
            uid=required_data[j],
            email=required_data[j]+'@abc.com',
            email_verified=True,
            password=required_data[j]+'@123@23@3',
            )
        print('Sucessfully created new user')


    print('everything is done properly!! :) :)')


browseButton_Excel = tk.Button(text='Import excel File', command=getexcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()