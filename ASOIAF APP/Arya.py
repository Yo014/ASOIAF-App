import customtkinter as ctk
from PIL import Image, ImageTk

class AryaBookI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arya Book I")
        self.root.geometry("555x600")
        self.root.eval('tk::PlaceWindow . center')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(root, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(root, width=450, height=100, state="disabled")
        self.text_box.place(x=15, y=405)

        self.create_buttons()

    def create_buttons(self):
        button_config = {
            "Arya I": {"command": self.show_AryaI, "position": (18, 496), "width": 120, "height": 40},
            "Arya II": {"command": self.show_AryaII, "position": (189, 496), "width": 120, "height": 40},
            "Arya III": {"command": self.show_AryaIII, "position": (369, 496), "width": 120, "height": 40},
            "Arya IV": {"command": self.show_AryaIV, "position": (18, 546), "width": 190, "height": 40},
            "Arya V": {"command": self.show_AryaV, "position": (279, 546), "width": 190, "height": 40},
            "Back": {"command": self.getback, "position": (20, 30), "width": 70, "height": 30}
        }

        for text, config in button_config.items():
            button = ctk.CTkButton(self.root, text=text, command=config["command"], width=config["width"], height=config["height"])
            button.place(x=config["position"][0], y=config["position"][1])

    def show_Arya_Chapters(self):
        return {
            "Arya I": {
                "image": "Arya_Stark.png",
                "text": "Arya I: Failing miserably at her needlework, Arya Stark goes to watch her brothers Robb and Bran practice swords with the princes Joffrey and Tommen, respectively."
            },
            "Arya II": {
                "image": "Arya_Stark.png",
                "text": "Arya II: Eddard comforts Arya over the death of her friend, the death of Sansa's direwolf, and the abandonment of her own wolf. A resolved Arya begins her first sword lesson with Syrio Forel."
            },
            "Arya III": {
                "image": "Arya_Stark.png",
                "text": "Arya III: While chasing cats, Arya stumbles into the middle of the Red Keep and overhears a conversation between two mysterious men. The two are plotting a war."
            },
            "Arya IV": {
                "image": "Arya_Stark.png",
                "text": "Arya IV: Ser Meryn comes to take Arya into custody while she is practicing with Syrio, who sacrifices himself so Arya can escape."
            },
            "Arya V": {
                "image": "Arya_Stark.png",
                "text": "Arya V: Arya watches in horror as Eddard is executed. She is grabbed by Yoren and taken into an alley."
            }
        }

    def show_AryaI(self): self.display_Arya("Arya I")
    def show_AryaII(self): self.display_Arya("Arya II")
    def show_AryaIII(self): self.display_Arya("Arya III")
    def show_AryaIV(self): self.display_Arya("Arya IV")
    def show_AryaV(self): self.display_Arya("Arya V")

    def display_Arya(self, Arya_name):
        profiles = self.show_Arya_Chapters()
        Arya_chapter = profiles[Arya_name]
        chapter_text = f"{Arya_chapter['text']}"
        self.update_text_box(chapter_text)
        self.update_image(Arya_chapter['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            tk_image = ImageTk.PhotoImage(pil_image)
            self.image_label.configure(image=tk_image)
            self.image_label.image = tk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")

    def getback(self):
        self.root.destroy()
        new_root = ctk.CTk()
        from POV_Characters import POVCharactersBookI
        POVCharactersBookI(new_root)
        new_root.mainloop()
