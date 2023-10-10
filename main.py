import customtkinter as c

def change_mode():
    if change_var.get() == "off":
        c.set_appearance_mode("light")
    else:
        c.set_appearance_mode("dark")

def add_item():
    item = entry.get()
    btncheck = c.CTkCheckBox(frame, text=item, width=10, height=5, font=("sans-serif", 13))
    btncheck.pack(pady=8, padx=10)

    delete = c.CTkButton(frame, text="Delete Item", fg_color="#720808", hover_color="#b90303", border_color="red"
                         , border_width=2, width=50, height=15, command=delete_item) 
    delete.pack(pady=8, padx=10)

def delete_item():
    print("item deleted")


c.set_appearance_mode("dark")
c.set_default_color_theme("green")

root = c.CTk()
root.geometry("400x550")

frame = c.CTkFrame(root)
frame.pack(pady=30, padx=40, fill="both", expand=True)

label = c.CTkLabel(frame, text="Todo List", font=("sans-serif", 18))
label.pack(pady=12, padx=10)

change_var = c.StringVar(value="on")
switch = c.CTkSwitch(frame, text="Light / Dark mode", variable=change_var,
                        offvalue="off", onvalue="on", command=change_mode)
switch.pack()


entry = c.CTkEntry(frame, placeholder_text="Enter Item", font=("sans-serif", 15), width=250, height=30)
entry.pack(pady=12, padx=10)

btn = c.CTkButton(frame, text="Add Item", width=100, height=30, command=add_item)
btn.pack(pady=12, padx=10)

root.mainloop()