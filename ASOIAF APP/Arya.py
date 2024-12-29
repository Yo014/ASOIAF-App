import tkinter as tk
from PIL import Image, ImageTk

class AryaBookI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arya BookI")
        self.root.geometry("555x600")
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg="light blue")
        
            # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=130, y=10)  # Adjust placement
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=65, height=5, state="disabled")
        self.text_box.place(x=15, y=405)

        self.create_buttons()
    def create_buttons(self):
        button_config = {  
            "Arya I": {"command": self.show_AryaI, "position": (18, 496), "width": 18, "height": 2},
            "Arya II": {"command": self.show_AryaII, "position": (189, 496), "width": 19, "height": 2},
            "Arya III": {"command": self.show_AryaIII, "position": (369, 496), "width": 18, "height": 2},
            "Arya IV": {"command": self.show_AryaIV, "position": (18, 546), "width": 28, "height": 2},
            "Arya V": {"command": self.show_AryaV, "position": (279, 546), "width": 28, "height": 2},

            "Back": {"command": self.getback, "position": (20, 30), "width": 5, "height": 1}           
        }

        for text, config in button_config.items():
            button = tk.Button(self.root, text=text, command=config["command"], bg="WHITE",  font=("Arial", 13), width=config["width"], height=config["height"])
            button.place(x=config["position"][0], y=config["position"][1])
    def show_Arya_Chapters(self):
        return{
            "Arya I":{
                "image":"Arya_Stark.png",
                "text": "Arya I:Failing miserably at her needlework, Arya Stark goes to watch her brothers Robb and Bran practice swords with the princes Joffrey and Tommen, respectively."
            },
            "Arya II":{
                "image":"Arya_Stark.png",
                "text": "Arya II: Eddard comforts Arya over the death of her friend, the death of Sansa's direwolf, and the abandonment of her own wolf. A resolved Arya begins her first sword lesson with Syrio Forel."
            },
            "Arya III":{
                "image":"Arya_Stark.png",
                "text": "Arya III: While chasing cats, Arya stumbles into the middle of the Red Keep and overhears a conversation between two mysterious men. The two are plotting a war."
            },
            "Arya IV":{
                "image":"Arya_Stark.png",
                "text": "Arya IV: Ser Meryn comes to take Arya into custody while she is practicing with Syrio, who sacrifices himself so Arya can escape."
            },
            "Arya V":{
                "image":"Arya_Stark.png",
                "text": "Arya V: Arya watches in horror as Eddard is executed. She is grabbed by Yoren and taken into an alley. "
            }
        }  
    def show_AryaI(self):self.display_Arya("Arya I")
    def show_AryaII(self):self.display_Arya("Arya II")
    def show_AryaIII(self):self.display_Arya("Arya III")    
    def show_AryaIV(self):self.display_Arya("Arya IV")    
    def show_AryaV(self):self.display_Arya("Arya V")
    
    def display_Arya(self, Arya_name):
        profiles = self.show_Arya_Chapters()
        Arya_chapter=profiles[Arya_name]
        chapter_text=f" {Arya_chapter['text']}"
        self.update_text_box(chapter_text)
        self.update_image(Arya_chapter['image'])
    
    def update_text_box(self, text):
        """
        Update the text box with the provided text.

        Parameters
        ----------
        text : str
            The text to be displayed in the text box.

        Returns
        -------
        None
        """
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, text)
        self.text_box.config(state="disabled")
        
    def update_image(self, image_name):
        """
        Updates the image displayed in the character profile.

        Args:
            image_name (str): The name of the image file to be loaded.

        Raises:
            Exception: If there is an error loading the image, it prints an error message and updates the text box with a failure message.
        """
        try:
            ##image_path = f"/Users/santomukiza/Desktop/test/character_profile/Png Files/{image_name}"
            image_path=f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            tk_image = ImageTk.PhotoImage(pil_image)
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from POV_Characters import POVCharactersBookI
        POVCharactersBookI(new_root)
        new_root.mainloop()

