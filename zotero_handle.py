import os
import subprocess
import time
import webbrowser
from tkinter import *
from pynput.keyboard import Key, Controller
import pyperclip

window = Tk()
window.title("Zotero link handle")
window.geometry('400x200')

keyboard = Controller()

def clicked1():
    page_and_comment_str = pyperclip.paste()
    page_and_comment_list = page_and_comment_str.split(',')
    zotero_link = page_and_comment_list[0]
    page = page_and_comment_list[1]
    commend = page_and_comment_list[2]

    webbrowser.open(zotero_link)
    time.sleep(0.5)
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('m')
        keyboard.release('m')
    print('keyboard1-for-zotero-link.')
    time.sleep(0.5)
    file_link = pyperclip.paste()

    cmd = "PDFXEdit.exe /A page=" + page + ";comment=" + commend + ";zoom=100 " + "\"" + file_link + "\""

    os.chdir("C:\\Program Files\\Tracker Software\\PDF Editor")
    subprocess.Popen(args=cmd, shell=True)

    print("pdf has been opened.")
    pyperclip.copy(page_and_comment_str)
    zotero_page_comment_link.delete(0, END)

    # res = "Welcome to a new world，" + file_link_from_zotero.get()
    # lbl.configure(text=res)
    # file_link_from_zotero.destroy()
    # btn.grid_forget()

def clicked2():
    original_entry_str = original_entry.get()
    page_entry_str = page_entry.get()
    comment_entry_str = comment_entry.get()

    # ((((📑)):xxx))
    result_str = original_entry_str + ',' + page_entry_str + ',' + comment_entry_str
    full_str = '((((📑)):'+result_str + '))'

    pyperclip.copy(full_str)

    print("result generated.")
    comment_entry.delete(0, END)


    # res = "Welcome to a new world，" + file_link_from_zotero.get()
    # lbl.configure(text=res)
    # file_link_from_zotero.destroy()
    # btn.grid_forget()

lbl = Label(window, text="To open pdf on a specific position.")
lbl.grid(column=0, row=0)

lbl3 = Label(window, text="original link: ")
lbl3.grid(column=0, row=1)
original_entry = Entry(window, width=20)
original_entry.grid(column=1, row=1)

lbl4 = Label(window, text="page number: ")
lbl4.grid(column=0, row=2)
page_entry = Entry(window, width=20)
page_entry.grid(column=1, row=2)

lbl5 = Label(window, text="comment: ")
lbl5.grid(column=0, row=3)
comment_entry = Entry(window, width=20)
comment_entry.grid(column=1, row=3)

btn2 = Button(window, text="GENERATE", command=clicked2)
btn2.grid(column=0, row=4)

lbl2 = Label(window, text="The zotero-page-comment link（shadowed）: ")
lbl2.grid(column=0, row=5)
zotero_page_comment_link = Entry(window, width=20)
zotero_page_comment_link.grid(column=1, row=5)

btn = Button(window, text="OPEN from clipboard", command=clicked1)
btn.grid(column=0, row=6)

window.mainloop()

# zotero://select/library/items/9D9FCY6F,6,cb408bd8-3fd8-448d-a267559f0208b632
