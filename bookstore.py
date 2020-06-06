from tkinter import *
import tkinter.messagebox
import backend
window = Tk()

def get_selected_row(event):
    try:
        global select_tup
        index=list1.curselection()[0]
        select_tup = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, select_tup[1])
        e2.delete(0,END)
        e2.insert(END, select_tup[2])
        e3.delete(0,END)    
        e3.insert(END, select_tup[3])
        e4.delete(0,END)
        e4.insert(END, select_tup[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_book():
    Item1 = (year_text.get())
    Item2 = (isbn_text.get())
    Item3 = (title_text.get())
    Item4 = (author_text.get())
    if (Item1.isdigit() or Item2.isdigit()):
        backend.insert(title_text.get(),author_text.get(),year_text.get(), isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(), isbn_text.get()))
        tkinter.messagebox.showinfo("Data Accepted","Data Accepted, Well done!")
        return True
    else:
        tkinter.messagebox.showwarning("Incorrect Input","Year & ISBN  Fields can only accept numbers and Title & Author fields only accept Alphabets")
        return False

def delete_book():
    backend.delete(select_tup[0])

def update_book():
    backend.update(select_tup[0], title_text.get(),author_text.get(),year_text.get(), isbn_text.get())

def reset_command():
    title_text.set("")    
    author_text.set("")
    year_text.set("")
    isbn_text.set("")
    return

#=======================Labels=======================
window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)


#=======================Entry Widgets=======================

title_text = StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable= author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable= year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable= isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column =0, rowspan=6, columnspan=2)

list1.bind("<<ListboxSelect>>", get_selected_row)

sb1 =Scrollbar(window)
sb1.grid(row=2, column=2 ,rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#=======================Buttons=======================

b1 =Button(window, text= "View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 =Button(window, text= "Search Book", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 =Button(window, text= "Add Book", width=12, command=add_book)
b3.grid(row=4, column=3)

b4 =Button(window, text= "Update", width=12, command=update_book)
b4.grid(row=5, column=3)

b5 =Button(window, text= "Delete", width=12, command=delete_book)
b5.grid(row=6, column=3)

b7 =Button(window, text= "Reset", width=12, command=reset_command)
b7.grid(row=7, column=3)


b6 =Button(window, text= "Close", width=12, command=window.destroy)
b6.grid(row=8, column=3)


window.mainloop()
