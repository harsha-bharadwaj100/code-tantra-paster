from time import sleep
import tkinter as tk
import pyautogui as pg
def paste_code():
    code = text_input.get("1.0", tk.END)
    print(code)
    sleep(2)
    pg.typewrite(code)

root = tk.Tk()
root.title("Code Paster")

# Create a text input widget
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Create a button widget
paste_button = tk.Button(root, text="Paste", command=paste_code)
paste_button.pack()
root.mainloop()