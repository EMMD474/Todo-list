import customtkinter as c

class Create_gui():
    c.set_appearance_mode("dark")
    c.set_default_color_theme("green")

    root = c.CTk()
    root.geometry("450x500")

    frame = c.CTkFrame(root)
    frame.pack(pady=30, padx=60, fill="both", expand=True)

    label = c.CTkLabel(frame, text="Todo-List", text_color="teal", font=("sans-serif", 18))
    label.pack(pady=12, padx=10)

    switch_var = c.StringVar(value="on")
    switch = c.CTkSwitch(frame, text="Light / Dark Mode", variable=switch_var, onvalue="on", offvalue="off"
                        , command=change_mode)
    switch.pack(pady=12, padx=10)

def change_mode():
    if switch_var.get() == "off":
            c.set_appearance_mode("light")
    else:
            c.set_appearance_mode("dark")
