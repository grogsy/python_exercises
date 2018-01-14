import tkinter as tk
import tkinter.messagebox as msg
import os
import sqlite3

class Todo(tk.Tk):

    def __init__(self):

        super().__init__()

        self.tasks = []

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.
                                  tasks_canvas.yview)

        # Set scrollbar values to the canvas
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("To-Do App")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Have the canvas draw the tasks frame inside itself
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.
                                                        tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()            # Have focus set to text widget

        todo1 = tk.Label(self.tasks_frame, text="---Add Items Here---", bg="lightgrey",
                     fg="black", pady=10)
        todo1.bind("<Button-1>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure) # Configure here means to resize the window
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [
            {
                "bg": "lightgrey", "fg": "black"
            },
            {
                "bg": "grey", "fg": "white"
            }
        ]

        # Load tasks from database
        saved_tasks = self.load_tasks()
        for task in saved_tasks:
            task_text = task[0]
            self.add_task(None, task_text, True)

    # Task handling methods
    def add_task(self, event=None, task_text=None, from_db=False):
        if not task_text:
            task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

            if not from_db:
                self.save_task(task_text)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget         # Events here are keypresses bound at instantiation
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)

            delete_task_query = "DELETE FROM tasks WHERE task=?"
            delete_task_data = (task.cget("text"),)
            self.runQuery(delete_task_query, delete_task_data)

            event.widget.destroy()

            self.recolour_tasks()
    # End task handling methods

    # Database handling methods
    def save_task(self, task):
        insert_task_query = "INSERT INTO tasks VALUES (?)"
        insert_task_data = (task,)
        self.runQuery(insert_task_query, insert_task_data)

    def load_tasks(self):
        load_tasks_query = "SELECT task FROM tasks"
        my_tasks = self.runQuery(load_tasks_query, receive=True)

        return my_tasks

    @staticmethod
    def runQuery(command, data=None, receive=False):
        conn = sqlite3.connect("tasks.db")
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

    @staticmethod
    def firstTimeDB():
        create_tables = "CREATE TABLE tasks (task TEXT)"
        Todo.runQuery(create_tables)

        default_task_query = "INSERT INTO tasks VALUES (?)"
        default_task_data = ("--- Add Items Here ---",)
        Todo.runQuery(default_task_query, default_task_data)
    # End database methods

    # Task colouring methods
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])
    # End task colouring methods

    # App resizing methods
    def on_frame_configure(self, event=None):
        # Sets the scrollable region for for the canvas whenever the window is resized
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        # Ensures the labels stay at whichever width the window is resized to
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)
    # End app resizing methods

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

if __name__=="__main__":
    if not os.path.isfile("tasks.db"):
        Todo.firstTimeDB()
    todo = Todo()
    todo.mainloop()

