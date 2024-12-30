# import tkinter as tk


# root = tk.Tk()
# root.title("Character Profile Viewer")
# root.geometry("600x600")  # Set window size
# # Image display area
# my_image =tk.PhotoImage(file="/Users/santomukiza/Desktop/test/character_profile/eddard_stark.png")
# lbl=tk.Label(image=my_image).pack()

# # Profile display area\
# root.mainloop()


import customtkinter as ctk
from PIL import Image

root = ctk.CTk()
root.geometry("600x600")

image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Catelyn_Stark.png"
image = Image.open(image_path)
resized_image = image.resize((100, 100))  # Resize image to fit the UI
photo = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(300, 462))  # Convert to CTkImage

# Define button action
def on_button_click():
    root.destroy()
    from Book_Summary import BookSummary_BookI
    new_root = ctk.CTk()
    BookSummary_BookI(new_root)
    new_root.mainloop()

# Create button with image
button = ctk.CTkButton(root, text="" ,image=photo, command=on_button_click,height=100, width=100,fg_color="transparent",bg_color="transparent", hover=False)
button.image=photo
button.pack()
root.mainloop()