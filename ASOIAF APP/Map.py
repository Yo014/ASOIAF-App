import customtkinter as ctk
from PIL import Image
from ASOIAF_APP import MainMenuPage

class MapsofASOIAF(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize image_label
        self.image_label = ctk.CTkLabel(self, text="")
        
        self.image_label.place(x=100, y=0)
        
        self.create_buttons()

    def create_buttons(self):
        button_config = {
            "Westoros": self.show_westoros,
            "Essos": self.show_essos,
            "Back":lambda: self.controller.show_frame(MainMenuPage)
        }
        positions = [
            (10, 950), (10, 900), (10, 30)
        ]
        for (text, command), (x, y) in zip(button_config.items(), positions):
            button = ctk.CTkButton(self, text=text, command=command , width=50, height=40)
            button.place(x=x, y=y)
    
    def maps(self):
        return {
            "Westoros": {
                "image": "Westoros.png",
            },
            "Essos": {
                "image": "Essos.png",
            }
        }

    def show_westoros(self):
        self.display_map("Westoros")
    
    def show_essos(self):
        self.display_map("Essos")
    
    def display_map(self, map_name):
        map_details = self.maps().get(map_name)
        if map_details:
            self.update_image(map_details['image'])
    
    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            image = Image.open(image_path)
            image = image.resize((900, 900))
            photo = ctk.CTkImage(image, size=(900, 1000))
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")

