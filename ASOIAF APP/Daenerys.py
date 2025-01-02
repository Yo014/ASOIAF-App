import customtkinter as ctk
from PIL import Image

class DaenerysBookI(ctk.CTkFrame):
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
                from_=1, to=10, number_of_steps=10,
                command=self.slider_changed, 
                width=400, 
                progress_color="purple",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Daenerys {self.convert_to_roman(chapter_index)}"
        self.display_Daenerys(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    
    def show_Daenerys_chapter(self):
        return {
            "Daenerys I": {
                "content": "Daenerys I content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys II": {
                "content": "Daenerys II content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys III": {
                "content": "Daenerys III content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys IV": {
                "content": "Daenerys IV content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys V": {
                "content": "Daenerys V content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys VI": {
                "content": "Daenerys VI content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys VII": {
                "content": "Daenerys VII content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys VIII": {
                "content": "Daenerys VIII content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys IX": {
                "content": "Daenerys IX content",
                "image": "Daenerys_Targaryen.png"
            },
            "Daenerys X": {
                "content": "Daenerys X content",
                "image": "Daenerys_Targaryen.png"
            }


          
        }
    def display_Daenerys(self, daenerys_name):
        profiles = self.show_Daenerys_chapter()
        Daenerys_chapter = profiles[daenerys_name]
        chapter_text = f"{Daenerys_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Daenerys_chapter['image'])
        
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