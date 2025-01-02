import customtkinter as ctk
from PIL import Image

class SansaBookI(ctk.CTkFrame):
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
                from_=1, to=6, number_of_steps=6,
                command=self.slider_changed, 
                width=400, 
                progress_color="orange",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Sansa {self.convert_to_roman(chapter_index)}"
        self.display_Sansa(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    
    def show_Sansa_chapter(self):
        return {
            "Sansa I": {
                "content": "Sansa I content",
                "image": "Sansa_Stark.png"
            },
            "Sansa II": {
                "content": "Sansa II content",
                "image": "Sansa_Stark.png"
            },
            "Sansa III": {
                "content": "Sansa III content",
                "image": "Sansa_Stark.png"
            },
            "Sansa IV": {
                "content": "Sansa IV content",
                "image": "Sansa_Stark.png"
            },
            "Sansa V": {
                "content": "Sansa V content",
                "image": "Sansa_Stark.png"
            },
            "Sansa VI": {
                "content": "Sansa VI content",
                "image": "Sansa_Stark.png"
            },
     

        }
    def display_Sansa(self, sansa_name):
        profiles = self.show_Sansa_chapter()
        Sansa_chapter = profiles[sansa_name]
        chapter_text = f"{Sansa_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Sansa_chapter['image'])
        
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