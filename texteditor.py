import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get('1.0', tk.END))


def clear_text():
    text_area.delete('1.0', tk.END)


def copy_text():
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)


def cut_text():
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)


def paste_text():
    clipboard_text = root.clipboard_get()
    text_area.insert(tk.INSERT, clipboard_text)


def select_all_text(event=None):
    text_area.tag_add(tk.SEL, '1.0', tk.END)
    text_area.mark_set(tk.INSERT, '1.0')
    text_area.see(tk.INSERT)
    return 'break'


def about():
    messagebox.showinfo('About', 'Simple Text Editor\n\nCreated with Python and Tkinter')


root = tk.Tk()
root.title("Text Editor")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=select_all_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Format", menu=format_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root)
text_area.pack()

root.bind('<Control-a>', select_all_text)


root.mainloop()