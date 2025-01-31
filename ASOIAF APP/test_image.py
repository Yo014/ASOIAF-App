# import tkinter as tk


# root = tk.Tk()
# root.title("Character Profile Viewer")
# root.geometry("600x600")  # Set window size
# # Image display area
# my_image =tk.PhotoImage(file="/Users/santomukiza/Desktop/test/character_profile/eddard_stark.png")
# lbl=tk.Label(image=my_image).pack()

# # Profile display area\
# root.mainloop()


# import customtkinter as ctk
# from PIL import Image

# root = ctk.CTk()
# root.geometry("600x600")

# image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Catelyn_Stark.png"
# image = Image.open(image_path)
# resized_image = image.resize((100, 100))  # Resize image to fit the UI
# photo = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(300, 462))  # Convert to CTkImage

# # Define button action
# def on_button_click():
#     root.destroy()
#     from Book_Summary import BookSummary_BookI
#     new_root = ctk.CTk()
#     BookSummary_BookI(new_root)
#     new_root.mainloop()

# # Create button with image
# button = ctk.CTkButton(root, text="" ,image=photo, command=on_button_click,height=100, width=100,fg_color="transparent",bg_color="transparent", hover=False)
# button.image=photo
# button.pack()
# root.mainloop()

from CTkScrollableDropdown import *
import customtkinter

root = customtkinter.CTk()

customtkinter.CTkLabel(root, text="Different Dropdown Styles").pack(pady=5)

# Some option list
values = ["python","tkinter","customtkinter","widgets",
          "options","menu","combobox","dropdown","search"]

# Attach to OptionMenu 
optionmenu = customtkinter.CTkOptionMenu(root, width=240)
optionmenu.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(optionmenu, values=values)

# Attach to Combobox
combobox = customtkinter.CTkComboBox(root, width=240)
combobox.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(combobox, values=values, justify="left", button_color="transparent")

# Attach to Entry
customtkinter.CTkLabel(root, text="Live Search Values").pack()

entry = customtkinter.CTkEntry(root, width=240)
entry.pack(fill="x", padx=10, pady=10)

# method to insert the chosen option from the autocomplete
def insert_method(e):
    entry.delete(0, 'end')
    entry.insert(0, e)

CTkScrollableDropdown(entry, values=values, command=lambda e: insert_method(e),
                      autocomplete=True) # Using autocomplete

button = customtkinter.CTkButton(root, text="choose options", width=240)
button.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(button, values=values, height=270, resize=False, button_height=30,
                      scrollbar=False, command=lambda e: button.configure(text=e))

root.mainloop()