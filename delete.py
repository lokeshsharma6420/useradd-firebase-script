import tkinter as tk
from tkinter import filedialog
import xlrd
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials


root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
canvas1.pack()


def getexcelnew():
    path = filedialog.askopenfilename()
    workbook = xlrd.open_workbook(path, "rb")                                                                                     #path of excel (xlsx )
    sheets = workbook.sheet_names()
    required_data = []

    for sheet_name in sheets:
        sh = workbook.sheet_by_name(sheet_name)
        for rownum in range(sh.nrows):                                                                                           #sheet.nrows for total no. of rows
          row_valaues = sh.row_values(rownum)
          noob=int(row_valaues[0])
          required_data.append((str(noob)))
    cred = credentials.Certificate("service credential file ")                                                                      #credentials file link
    firebase_admin.initialize_app(cred)

    for i in range(1,sh.nrows):
        user = auth.delete_user(
            uid=required_data[i]+'@abc.com',
        )
        print('Sucessfully deleted user')


    print('task done')




browseButton_Excel = tk.Button(text='Import excel File [delete Task]', command=getexcelnew, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()