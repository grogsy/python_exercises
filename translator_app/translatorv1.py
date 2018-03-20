import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

import requests

class Translator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Translation Book")
        self.geometry("500x300")

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")

        self.lang_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.lang_menu.add_command(label="Portuguese", command=self.
                                   add_portuguese_tab)

        self.menu.add_cascade(label="Language", menu=self.lang_menu)
        self.config(menu=self.menu)

        self.notebook = Notebook(self)

        english_tab = tk.Frame(self.notebook)
        italian_tab = tk.Frame(self.notebook)

        self.itranslation = tk.StringVar(italian_tab)
        self.itranslation.set("")

        self.tbutton = tk.Button(english_tab, text="Translate", command=lambda
                                 langs=["it"], elems=[self.itranslation]: self.translate(langs, None, elems))
        self.tbutton.pack(side=tk.BOTTOM, expand=1)

        self.txt_field = tk.Text(english_tab, bg="white", fg="black")
        self.txt_field.pack(side=tk.TOP, expand=1)
        self.txt_field.focus_set()

        self.ibutton = tk.Button(italian_tab, text="Copy to Clipboard",
                                 command=self.copy_to_clipboard)
        self.ibutton.pack(side=tk.BOTTOM, fill=tk.X)

        self.ilabel = tk.Label(italian_tab, textvar=self.itranslation, bg=
                               "lightgrey", fg="black")
        self.ilabel.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(english_tab, text="English")
        self.notebook.add(italian_tab, text="Italian")
        self.notebook.pack(fill=tk.BOTH, expand=1)

    def translate(self, target_languages=None, text=None, elements=None):
        if not text:
            text = self.txt_field.get(1.0, tk.END)
        if not elements:
            elements = [self.itranslation]
        if not target_languages:
            target_languages = ["it"]

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}"

        try:
            for code, element in zip(target_languages, elements):
                full_url = url.format("en", code, text)
                r = requests.get(full_url, verify=False) # Set verify to false, to avoid "cert verify failed" error 
                r.raise_for_status()
                translation = r.json()[0][0][0]
                element.set(translation)
        except Exception as e:
            msg.showerror("Translation failed", str(e))
            print(str(e))
            print(e)
        finally:
            msg.showinfo("Translation Successful", "Text successfully translated")

    def copy_to_clipboard(self,text=None):
        if not text:
            text = self.itranslation.get()

        self.clipboard_clear()
        self.clipboard_append(text)
        msg.showinfo("Copied Successfully", "Text copied to clipboard")

    def add_portuguese_tab(self):
        portuguese_tab = tk.Frame(self.notebook)
        self.ptranslation = tk.StringVar(portuguese_tab)
        self.ptranslation.set("")

        self.p_copy_button = tk.Button(portuguese_tab, text="Copy to Clipboard",
                                       command=lambda: self.copy_to_clipboard(self.ptranslation.get()))
        self.p_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.plabel = tk.Label(portuguese_tab, textvar=self.ptranslation, bg="lightgrey", fg="black")
        self.plabel.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(portuguese_tab, text="Portuguese")

        self.lang_menu.entryconfig("Portuguese", state="disabled")

        self.tbutton.config(command=lambda langs=["it", "pt"], elems=[self.itranslation, self.ptranslation]:
                            self.translate(langs, None, elems))


if __name__ == "__main__":
    translator = Translator()
    translator.mainloop()

