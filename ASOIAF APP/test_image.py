# import tkinter as tk


# root = tk.Tk()
# root.title("Character Profile Viewer")
# root.geometry("600x600")  # Set window size
# # Image display area
# my_image =tk.PhotoImage(file="/Users/santomukiza/Desktop/test/character_profile/eddard_stark.png")
# lbl=tk.Label(image=my_image).pack()

# # Profile display area\
# root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x600")

image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/character_profile/Png Files/Catelyn_Stark.png"
image = Image.open(image_path)
resized_image = image.resize((100, 100))  #Resize image to fit the UI
photo = ImageTk.PhotoImage(resized_image)  #Convert to PhotoImage

Button = tk.Button(root, text="Click Me", image=photo)
Button.image=photo
# Define button action
def on_button_click():
    print("Button clicked!")

# Create button with image
button = tk.Button(root, image=photo, command=on_button_click, borderwidth=0)
button.image = photo  # Keep a reference to avoid garbage collection
button.pack()
root.mainloop()