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
            "Image": "Catelyn_Stark.png"
        }
        character_profile_arya= {
            "Name": "Arya Stark",
            "House": "House Stark of Winterfell",
            "Titles": [""],
            "Bio": "Arya Stark",
            "Image": "Arya_Stark.png"
        }
        chararacter_profile_sansa= {
            "Name": "Sansa Stark",
            "House": "House Stark of Winterfell",
            "Titles": [""],
            "Bio": "Sansa Stark",
            "Image": "Sansa_Stark.png"
        }
        chararacter_profile_daenerys= {
            "Name": "Daenerys Targaryen",
            "House": "House Targaryen of Dragonstone",
            "Titles": [""],
            "Bio": "Daenerys Targaryen",
            "Image": "Daenerys_Targaryen.png"
        }
        character_profile_bran= {
            "Name": "Bran Stark",
            "House": "House Stark of Winterfell",
            "Titles": [""],
            "Bio": "Bran Stark",
            "Image": "Bran_Stark.png"
            
        }
        return character_profile_eddard, character_profile_tyrion, character_profile_Jon, character_profile_caetlyn, character_profile_arya, chararacter_profile_sansa, chararacter_profile_daenerys, character_profile_bran
    
    ##return character_profile()
    return character_profile()

    # Function to display the profile
# Function to display Eddard's profile
def show_profile1():
    profiles = book1_A_Game_of_Thrones()
    character_profile_eddard = profiles[0]
    display_profile(character_profile_eddard)

# Function to display Tyrion's profile
def show_profile2():
    profiles = book1_A_Game_of_Thrones()
    character_profile_tyrion = profiles[1]
    display_profile(character_profile_tyrion)
def show_profile3():
    profiles = book1_A_Game_of_Thrones()
    character_profile_Jon = profiles[2]
    display_profile(character_profile_Jon)

def show_profile4():
    profiles = book1_A_Game_of_Thrones()
    character_profile_caetlyn = profiles[3]
    display_profile(character_profile_caetlyn)

def show_profile5():
    profiles = book1_A_Game_of_Thrones()
    character_profile_arya = profiles[4]
    display_profile(character_profile_arya)  

def show_profile6():
    profiles = book1_A_Game_of_Thrones()
    character_profile_sansa = profiles[5]
    display_profile(character_profile_sansa)    

def show_profile7():
    profiles = book1_A_Game_of_Thrones()
    character_profile_daenerys = profiles[6]
    display_profile(character_profile_daenerys)  

def show_profile8():
    profiles = book1_A_Game_of_Thrones()
    character_profile_bran = profiles[7]
    display_profile(character_profile_bran)

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
        resized_image = pil_image.resize((160, 200))  #Resize image to fit the UI
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
root.configure(bg="light blue")
# Image display area
image_label = tk.Label(root)
image_label = tk.Label(root, bg="light blue")
image_label.pack(pady=10)
# Profile display area
text_box = tk.Text(root, wrap=tk.WORD, width=80, height=15, state="disabled")
text_box.pack(pady=5)
text_box.place(x=15, y=220)


def buttons():
    button_bg = "light blue"

# Button to load the profile
    button_eddard = tk.Button(root, text="Eddard Stark", command=show_profile1,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0, )
    button_eddard.place(x=470, y=450)
    
    button_tyrion = tk.Button(root, text="Tyrion Lannister", command=show_profile2,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_tyrion.place(x=20, y=450)

    button_jon = tk.Button(root, text="Jon Snow", command=show_profile3,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_jon.place(x=263, y=450)

    button_caetlyn = tk.Button(root, text="Catelyn Stark", command=show_profile4,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_caetlyn.place(x=263, y=500)

    button_arya = tk.Button(root, text="Arya Stark", command=show_profile5,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_arya.place(x=470, y=500)

    button_daenerys = tk.Button(root, text="Daenerys Targaryen", command=show_profile7,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_daenerys.place(x=20, y=500)

    button_sansa = tk.Button(root, text="Sansa Stark", command=show_profile6,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_sansa.place(x=160, y=550)

    button_bran = tk.Button(root, text="Bran Stark", command=show_profile8,bg=button_bg, fg="black", borderwidth=0, highlightthickness=0)
    button_bran.place(x=350, y=550) 
    
    return button_bran, button_daenerys, button_sansa, button_arya, button_caetlyn, button_jon, button_tyrion, button_eddard  
buttons()
# Run the app
root.mainloop()