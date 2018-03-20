import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

import requests

import sqlite3
import os

class LanguageTab(tk.Frame):
    def __init__(self, master, lang_name, lang_code):
        super().__init__(master)

        self.lang_name = lang_name
        self.lang_code = lang_code

        self.translation_var = tk.StringVar(self)
        self.translation_var.set("")

        self.translated_label = tk.Label(self, textvar=self.translation_var, bg="lightgrey", fg="black")

        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.
                                     copy_to_clipboard)

        self.copy_button.pack(side=tk.BOTTOM, fill=tk.X)
        self.translated_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def copy_to_clipboard(self):
        root = self.winfo_toplevel()
        root.clipboard_clear()
        root.clipboard_append(self.translation_var.get())
        msg.showinfo("Copied Successfully", "Text copied to clipboard")

class TranslateBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Translation Book")
        self.geometry("500x300")

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")

        self.languages_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")

        self.languages_menu.add_command(label="Add New", command=self.
                                        show_new_language_popup)
        
        # The default language.
        self.languages_menu.add_command(label="Filipino", command=lambda: self.
                                        add_new_language(LanguageTab(self, "Filipino", "tl")))

        self.remove_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")

        # Configure the languages_menu to be a drop-down menu
        self.menu.add_cascade(label="Languages", menu=self.languages_menu)
        self.menu.add_cascade(label="Remove", menu=self.remove_menu)

        self.config(menu=self.menu)

        self.notebook = Notebook(self)

        self.language_tabs = {}

        english_tab = tk.Frame(self.notebook)

        self.translate_button = tk.Button(english_tab, text="Translate", command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(english_tab, bg="white", fg="black")
        self.english_entry.pack(side=tk.TOP, expand=1)
        self.english_entry.focus_set()

        self.notebook.add(english_tab, text="English")

        self.notebook.pack(fill=tk.BOTH, expand=1)

        self.bind("<Return>", self.translate)

        saved_tabs = self.load_tabs()
        for row in saved_tabs:
            lang, code = row
            tab = LanguageTab(self, lang, code)
            self.languages_menu.add_command(label=lang, command=lambda: self.
                                            add_new_language(tab, from_db=True))

    def add_new_language(self, language, from_db=False):
        self.language_tabs[language.lang_name] = language

        self.notebook.add(language, text=language.lang_name)
        self.remove_menu.add_command(label=language.lang_name, command=lambda: self.
                                     remove_language(language))
        if not from_db:
            self.save_tab_info(label=language.lang_name, code=language.lang_code)
        try:
            self.languages_menu.entryconfig(language.lang_name, state="disabled")
        except:
            pass

    def remove_language(self, language):
        if msg.askyesno("Careful", "Delete entry?"):
            # Difficult to delete menu option by index, so we do it by its label instead(language.lang_name)
            self.languages_menu.delete(language.lang_name)
            self.remove_menu.delete(language.lang_name)

            delete_label = "DELETE FROM tabs where language=?"
            delete_code  = "DELETE FROM tabs where code=?"
            self.run_query(delete_label, (language.lang_name,))
            self.run_query(delete_code, (language.lang_code,))

            language.destroy()
            del self.language_tabs[language.lang_name]
        else:
            pass

    def show_new_language_popup(self):
        NewLanguageForm(self)

    def translate(self, text=None, event=None):
        if len(self.language_tabs) < 1:
            msg.showerror("No Languages", "No languages added. Please add some from the menu")
            return

        if not text:
            text = self.english_entry.get(1.0, tk.END).strip()

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}"

        try:
            for language in self.language_tabs.values():
                full_url = url.format("en", language.lang_code, text)
                r = requests.get(full_url, verify=False)
                r.raise_for_status()
                translation = r.json()[0][0][0]
                language.translation_var.set(translation)
        except Exception as e:
            msg.showerror("Translation Failed", str(e))
        else:
            msg.showinfo("Translation Successful", "Text successfully translated")

    # Database methods
    @staticmethod
    def create_session():
        create_tables = "CREATE TABLE tabs (language TEXT, code TEXT)"
        TranslateBook.run_query(create_tables)

    @staticmethod
    def run_query(command, data=None, receive=False):
        conn = sqlite3.connect("session.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(command, data)
        else:
            cursor.execute(command)
        if receive:
            return cursor.fetchall()
        else:
            conn.commit()
        conn.close()

    def save_tab_info(self, label, code):
        insert_tab_query = "INSERT INTO tabs(language, code) VALUES(?,?)"
        self.run_query(insert_tab_query, (label, code))

    def load_tabs(self):
        load_tabs_query = "SELECT language, code FROM tabs"
        tabs = self.run_query(load_tabs_query, receive=True)

        return tabs

class NewLanguageForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__()

        self.master = master

        self.title("Add new Language")
        self.geometry("300x150")

        self.name_label = tk.Label(self, text="Language Name")
        self.name_entry = tk.Entry(self, bg="white", fg="black")
        self.code_label = tk.Label(self, text="Language Code")
        self.code_entry = tk.Entry(self, bg="white", fg="black")
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)

        self.name_label.pack(fill=tk.BOTH, expand=1)
        self.name_entry.pack(fill=tk.BOTH, expand=1)
        self.code_label.pack(fill=tk.BOTH, expand=1)
        self.code_entry.pack(fill=tk.BOTH, expand=1)
        self.submit_button.pack(fill=tk.X)

        self.name_entry.focus_set()
        self.bind("<Return>", self.submit)

    def submit(self, event=None):
        lang_name = self.name_entry.get()
        lang_code = self.code_entry.get()

        if lang_name and lang_code:
            new_tab = LanguageTab(self.master, lang_name, lang_code)
            self.master.languages_menu.add_command(label=lang_name, command=lambda: self.
                                                   master.add_new_language(new_tab))
            msg.showinfo("Language Option Added", "Language option " + lang_name + " added to menu")
            self.destroy()
        else:
            msg.showerror("Missing Information", "Please add both a name and code")


if __name__ == "__main__":
    if not os.path.isfile("session.db"):
        TranslateBook.create_session()
    t = TranslateBook()
    t.mainloop()

