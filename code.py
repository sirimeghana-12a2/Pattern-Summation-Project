from tkinter import*
from PIL import ImageTk,Image
import numpy as np 
import tkinter as tk


def get_table(lst, c):
    rows = len(lst) // c
    if len(lst) % c != 0:
        rows += 1
    table = np.zeros((rows, c), dtype=int)
    space=(c*rows)-len(lst)
    for i in range(c):
        if i==(c-space):
         rows=rows-1
        l1=[]
        for k in range(rows):
          x=lst.pop(0)
          l1.append(x)
          lst.append(x)
        for j in range(rows):
          table[j,i]=l1[j]  
    return table

def create_table():
    data = [int(num) for num in num_entry.get().split()]
    c = int(c_entry.get())
    table = get_table(data,c)
    row_sums = np.sum(table, axis=1)
    result_text = f"C\tROW SUMS\n\t"
    result_text += f"{c}\t "
    for i in range(table.shape[0]):
        result_text += f"{row_sums[i]} "
    result_text += "\n" + "*" * 20
    result_label.config(text=result_text)
   
    table_text = "\n".join(["\t".join(map(str, row)) for row in table])
    table_label.config(text=table_text)
    


# Create the main window
window = tk.Tk()
window.title("Pattern summation")
image_0=Image.open('C:\\Users\Dell\Downloads\\PSphoto.png')
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(window,image=bck_end)
lbl.place(x=0,y=0)
window.attributes('-fullscreen',True)

# Create the button to exit the window
exit1=Image.open('C:\\Users\Dell\Downloads\\exit.jpeg')
back_end=ImageTk.PhotoImage(exit1)
exit_button = tk.Button(window,image=back_end, command=window.destroy)
exit_button.place(x=1200,y=0)


# Create the input widgets
num_label = tk.Label(window, text="Enter numbers (separated by spaces):",font=('aerial',15,'italic'))
num_label.grid(row=0, column=150, padx=15, pady=15)
num_entry = tk.Entry(window,font=('aerial',15,'italic'))
num_entry.grid(row=1, column=150, padx=15, pady=15)

c_label = tk.Label(window, text="Enter number of columns:",font=('aerial',15,'italic'))
c_label.grid(row=2, column=150, padx=10, pady=10)
c_entry = tk.Entry(window,font=('aerial',15,'italic'))
c_entry.grid(row=3, column=150, padx=10, pady=10)

# Create the button to generate the table
generate_button = tk.Button(window, text="Generate Table",font=('aerial',15,'italic'),bg='navy',fg='white', command=create_table)
generate_button.grid(row=9, column=150, padx=5, pady=5,columnspan=100)

   
# Create the label to display the table sums
result_label = tk.Label(window, text="", font=("aerial", 13,'italic'))
result_label.grid(row=5, column=150, padx=5, pady=5, columnspan=100, sticky='n')

# Create the label to display the table
table_label = tk.Label(window, text="",font=('aerial',13,'italic'))
table_label.grid(row=6, column=150, padx=5, pady=5,columnspan=100, sticky='n')

# Center the table and its sums
window.grid_rowconfigure(150, weight=1)
window.grid_rowconfigure(150, weight=1)
window.grid_columnconfigure(150, weight=1)

# Start the main loop
window.mainloop()
