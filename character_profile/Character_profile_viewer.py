import tkinter as tk
from PIL import Image, ImageTk

def book1_A_Game_of_Thrones():
    # Character data sample
    def character_profile():
        character_profile_eddard = {
            "Name": "Eddard Stark",
            "House": "Stark of Winterfell",
            "Titles": ["Lord of Winterfell", "Warden of the North", "Hand of the King"],
            "Bio": "Eddard 'Ned' Stark was the Lord of Winterfell and head of House Stark. "
                "He was known for his honor and loyalty, which ultimately led to his tragic fate.",
            "Image": "eddard_stark.png"
        }
        character_profile_tyrion = {
            "Name": "Tyrion Lannister",
            "House": "House Lannister of Casterly Rock",
            "Titles": [ "Hand of the King", "The Imp","Little Demon"],
            "Bio": "Tyrion 'Tywin' Lannister was the King in the North and head of House Lannister. ",
            "Image": "Tyrion_lannister.png"
        }
        character_profile_Jon = {
            "Name": "Jon Snow",
            "House": "House Stark of Winterfell",
            "Titles": ["bastard of winterfell", "Lord Snow"],
            "Bio": "Jon Snow bastard son of Eddard Stark",
            "Image": "Jon_Snow.png"
        }
        character_profile_caetlyn = {
            "Name": "Caetlyn Stark",
            "House": "House Stark of Winterfell, House Tully",
            "Titles": ["Lady of Winterfell"],
            "Bio": "Caetlyn  Stark",
            "Image": "Caetlyn_Stark.png"
        }
        return character_profile_eddard, character_profile_tyrion, character_profile_Jon, character_profile_caetlyn
    
    ##return character_profile()
    return character_profile()

    # Function to display the profile
# Function to display Eddard's profile
def show_profile1():
    character_profile_eddard, _, _ = book1_A_Game_of_Thrones()
    display_profile(character_profile_eddard)

# Function to display Tyrion's profile
def show_profile2():
    _, character_profile_tyrion, _, _ = book1_A_Game_of_Thrones()
    display_profile(character_profile_tyrion)
def show_profile3():
    _,_, character_profile_Jon = book1_A_Game_of_Thrones()
    display_profile(character_profile_Jon)

def show_profile4():
    _,_, character_profile_caetlyn,_ = book1_A_Game_of_Thrones()
    display_profile(character_profile_caetlyn)

def display_profile(character_profile):
    profile_text = f"Name: {character_profile['Name']}\n" \
                f"House: {character_profile['House']}\n" \
                f"Titles: {', '.join(character_profile['Titles'])}\n" \
                f"Biography:{character_profile['Bio']}"

    # Function to update the text box
    update_text_box(profile_text)

    # Update the character ima
    update_image(character_profile)



def update_image(character_profile):
    try:
        image_path = f"/Users/santomukiza/Desktop/test/character_profile/Png Files/{character_profile['Image']}"
        pil_image = Image.open(image_path)  # Load the image using Pillow
        resized_image = pil_image.resize((150, 150))  #Resize image to fit the UI
        tk_image = ImageTk.PhotoImage(resized_image)  #Convert to PhotoImage
        image_label.config(image=tk_image)
        image_label.image = tk_image  #Keep a reference to avoid garbage collection
        image_label.pack()
    except Exception as e:
        print(f"Error loading image: {e}")
        text_box.insert(tk.END, "\n[Image could not be loaded.]")

# Function to update the text box
def update_text_box(profile_text):
    text_box.config(state="normal")  # Enable editing to update text
    text_box.delete(1.0, tk.END)  # Clear existing text
    text_box.insert(tk.END, profile_text)  # Insert new text
    text_box.config(state="disabled")  # Disable editing after inserting text
# Tkinter setup
root = tk.Tk()
root.title("Character Profile Viewer")
root.geometry("600x600")  # Set window size
# Image display area
image_label = tk.Label(root)
image_label.pack(pady=10)
# Profile display area
text_box = tk.Text(root, wrap=tk.WORD, width=800, height=15, state="disabled")
text_box.pack(padx=20, pady=20)


# Button to load the profile
button_eddard = tk.Button(root, text="Eddard Stark", command=show_profile1)
button_eddard.pack(pady=5)
button_eddard.place(x=150, y=400)

button_tyrion = tk.Button(root, text="Tyrion Lannister", command=show_profile2)
button_tyrion.pack(pady=5)
button_tyrion.place(x=20, y=400)

button_jon = tk.Button(root, text="Jon Snow", command=show_profile3)
button_jon.pack(pady=5)
button_jon.place(x=260, y=400)

button_caetlyn = tk.Button(root, text="Caetlyn Stark", command=show_profile4)
button_caetlyn.pack(pady=5)
button_caetlyn.place(x=370, y=400)
# Run the app
root.mainloop()