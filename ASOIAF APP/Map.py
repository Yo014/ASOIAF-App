import tkinter as tk
from PIL import Image, ImageTk
class MapsofASOIAF:
    def __init__(self, root):
        self.root = root
        self.root.title("Map of ASOIAF")
        self.root.geometry("1000x1000")
        self.root.configure(bg="light blue")
        
        # bg_image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Daenerys_Targaryen.png"
        # bg_image = Image.open(bg_image_path).resize((1000, 1000))
        # self.bg_photo = ImageTk.PhotoImage(bg_image)
        # self.bg_label = tk.Label(self.root, image=self.bg_photo)
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)       
        
        # Initialize image_label
        self.image_label = tk.Label(self.root, bg="light blue")
        self.image_label.place(x=200, y=0)
        
        self.create_buttons()
    def create_buttons(self):
        button_config={
            "Westoros":self.show_westoros,
            "Essos":self.show_essos,
            "Back":self.getback
            
        }
        positions=[
            (0, 950), (100, 950),(20,30)
        ]
        for (text, command), (x, y) in zip(button_config.items(), positions):
            button = tk.Button(self.root, text=text, command=command, bg="WHITE", relief=tk.FLAT)
            button.place(x=x, y=y)
            
    def maps(self):
        return{
            "Westoros":{
                "image":"Westoros.png",
            },
            "Essos":{
                "image":"Essos.png",
        }
    }
    
    def show_westoros(self):self.display_map("Westoros")
    def show_essos(self):self.display_map("Essos")
    def display_map(self, map_name):
        map_details = self.maps().get(map_name)
        if map_details:
            self.update_image(map_details['image'])
    def update_image(self, image_name):
        try:
            image_path=f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            image = Image.open(image_path).resize((800, 1000))
            tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
        except Exception as e:
            print(f"Error loading image: {e}")
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()
 