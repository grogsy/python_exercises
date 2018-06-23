''' Basic tkinter-based GUI program that fetches records from a database via python's shelve module.
    
    All records are stored in a 'Person' object which has basic fields such as name, age, job, and pay.
    The GUI supports fetching, updating, deleting and storing and adding records to the database.
'''

from tkinter import *
from tkinter.messagebox import showerror, showinfo, askyesno
import shelve

class App:

    def __init__(self, master):
        # we use this var in our closeApp method
        self.master = master

        # frame for our entries and labels
        form = Frame(master)
        form.pack(side=RIGHT)

        # where our Entry widgets(ent) will live
        self.entries = {}
        self.db = shelve.open('class-shelve')
        self.fields = ('name', 'age', 'job', 'pay')

        # create our label and input fields
        for (ix, label) in enumerate(('key',) + self.fields):
            lab = Label(form, text=label)
            ent = Entry(form)

            lab.grid(row=ix, column=0)
            ent.grid(row=ix, column=1)
            self.entries[label] = ent

        self.show_btn = Button(master, text= "Show Keys", command=self.showKeys).pack(side=LEFT)
        self.fetch_btn = Button(master, text="Fetch", command=self.fetchRecord).pack(side=LEFT)
        self.update_btn = Button(master, text="Update", command=self.updateRecord).pack(side=LEFT)
        self.clear_btn = Button(master, text="Clear", command=self.clearInput).pack(side=LEFT)
        self.delete_btn = Button(master, text="Remove", command=self.deleteKey).pack(side=LEFT)
        self.quit_btn = Button(master, text="Quit", command=self.closeApp).pack(side=RIGHT)

    def showKeys(self):
        lst = '\n'.join([k for k in sorted(list(self.db.keys()))])
        showinfo(title='Keys', message=str(lst))

    def clearInput(self):
        for field in (('key',) + self.fields):
            self.entries[field].delete(0, END)

    def deleteKey(self):
        key = self.entries['key'].get()
        warning = "You are about to delete this key,\
                 are you sure you want to do that?"
        if askyesno(title='Warning', message=warning):
            try:
                del self.db[key]
                App.clearInput(self)
                showinfo(title='Deleted', message='Key removed successfully')
            except KeyError:
                showinfo(title='Error', message='Key does not exist')
        else:
            pass

    def fetchRecord(self):
        key = self.entries['key'].get()
        try:
            record = self.db[key]
        except KeyError:
            showerror(title='Error', message='No such key!')
        else:
            for field in self.fields:
                self.entries[field].delete(0, END)
                self.entries[field].insert(0, getattr(record, field))

    def updateRecord(self):
        warning = "You are about to overwrite info for this person,\
                  are you sure you want to do that?"
        if askyesno(title='Warning', message=warning):
            key = self.entries['key'].get()
            if key in self.db:
                record = self.db[key]
            else:
                from person import Person
                record = Person(name='none', age='0')
            for field in self.fields:
                usr_input = self.entries[field].get()
                if all(c.isalpha() or c.isspace() \
                       for c in usr_input):
                    setattr(record, field, str(usr_input))
                elif usr_input.isdigit():
                    setattr(record, field, int(usr_input))
                else:
                    showerror('Error', message='One of the forms has \
                              invalid input')
            self.db[key] = record
            showinfo(title="Success", message="Record updated.")
        else:
            pass

    def closeApp(self):
        self.db.close()
        self.master.quit()

root = Tk()
root.title('People Shelve')
app = App(root)
root.mainloop()
