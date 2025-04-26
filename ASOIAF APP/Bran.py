import customtkinter as ctk
from PIL import Image

class BranBookI(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)  # Adjust placement  
        
        self.text_box=ctk.CTkTextbox(self,font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)
        
        self.create_slider()
        self.create_buttons()
    
    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
                from_=1, to=7, number_of_steps=11,
                command=self.slider_changed, 
                width=400, 
                progress_color="dark green",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Bran {self.convert_to_roman(chapter_index)}"
        self.display_Bran(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI", "VII"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    
    def show_Bran_chapter(self):
        return {
        "Bran I": {
            "content": "Bran I:Robb Stark and Jon Snow discover a litter of direwolves, one pup for each of Eddard Stark's six children.",
            "image": "Bran_Stark.png"
        },
        "Bran II": {
            "content": "Bran II:Bran accidentally witnesses Queen Cersei Lannister having sex with her twin brother, Ser Jaime Lannister of the Kingsguard. Jaime shoves Bran from a tower.",
            "image": "Bran_Stark.png"
        },
        "Bran III": {
            "content": "Bran III:After several cryptic dreams, Bran finally wakes from his coma. He names his direwolf Summer.",
            "image": "Bran_Stark.png"
        },
        "Bran IV": {
            "content": "Bran IV:Bran listens to Old Nan recount a tale about the Others when Tyrion Lannister returns to Winterfell, bearing a gift for the crippled boy.",
            "image": "Bran_Stark.png"
        },
        "Bran V": {
            "content": "Bran V:Bran takes his first ride outside Winterfell on Dancer and is accosted by a group of wildlings and Night's Watch deserters. They are all killed save a wildling named Osha.",
            "image": "Bran_Stark.png"
        },
        "Bran VI": {
            "content": "Bran VI:Robb has called the banners of the North and Bran hosts the Karstarks. Robb marches south.",
            "image": "Bran_Stark.png"
        },
        "Bran VII": {
            "content": "Bran VII:Maester Luwin tells Bran and Rickon about the children of the forest. A raven arrives announcing Eddard's death.",
            "image": "Bran_Stark.png"
        }
    }
    def display_Bran(self, bran_name):
        profiles = self.show_Bran_chapter()
        Bran_chapter = profiles[bran_name]
        chapter_text = f"{Bran_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Bran_chapter['image'])
        
    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")
        
    def update_image(self, image_name):
        
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")



class BranBookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)  # Adjust placement  

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self, 
            from_=1, to=6, number_of_steps=5,
            command=self.slider_changed, 
            width=400, 
            progress_color="dark green",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Bran {self.convert_to_roman(chapter_index)}"
        self.display_Bran(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI"]
        return roman_numerals[num-1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookII
        button_back = ctk.CTkButton(
            self, text="Back",
            command=lambda: self.controller.show_frame(POVCharactersBookII),
            width=80, height=30,
            corner_radius=8,
            bg_color="transparent",
            fg_color="transparent",
            hover_color="grey",
            font=("Arial", 18)
        )
        button_back.place(x=20, y=30)

    def show_Bran_chapter(self):
        return {
            "Bran I": {
                "content": "Bran I: Bran dreams of his father’s death and talks with Luwin about his strange dreams.",
                "image": "Bran_Stark.png"
            },
            "Bran II": {
                "content": "Bran II: As Winterfell prepares for war, Bran presides over the castle in Robb’s absence.",
                "image": "Bran_Stark.png"
            },
            "Bran III": {
                "content": "Bran III: Meera and Jojen Reed arrive at Winterfell and talk to Bran about his green dreams.",
                "image": "Bran_Stark.png"
            },
            "Bran IV": {
                "content": "Bran IV: Theon Greyjoy captures Winterfell and takes Bran and Rickon hostage.",
                "image": "Bran_Stark.png"
            },
            "Bran V": {
                "content": "Bran V: Bran and Rickon escape Winterfell with the help of Hodor, the Reeds, and Osha.",
                "image": "Bran_Stark.png"
            },
            "Bran VI": {
                "content": "Bran VI: Theon shows the charred bodies of two boys, claiming they are Bran and Rickon.",
                "image": "Bran_Stark.png"
            }
        }

    def display_Bran(self, bran_name):
        profiles = self.show_Bran_chapter()
        Bran_chapter = profiles[bran_name]
        chapter_text = f"{Bran_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Bran_chapter['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")

