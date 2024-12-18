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

image_path = "/Users/santomukiza/Desktop/test/character_profile/eddard_stark.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.image = photo  # keep a reference to prevent garbage collection
label.pack()

root.mainloop()