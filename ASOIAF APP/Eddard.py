import customtkinter as ctk
from PIL import Image

class EddardBookI(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)  # Adjust placement  
        
        self.text_box=ctk.CTkTextbox(self,font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)
        
        self.create_slider()
        self.create_buttons()
    
    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
                from_=1, to=15, number_of_steps=15,
                command=self.slider_changed, 
                width=400, 
                progress_color="dark blue",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)
    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Eddard {self.convert_to_roman(chapter_index)}"
        self.display_Eddard(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    def show_Eddard_Chapter(self):
        return {
        "Eddard I": {
            "content": "Eddard I:King Robert and his party arrive in Winterfell. Robert asks Eddard to be the new Hand of the King and promises to wed his son Joffrey to Ned's daughter Sansa.",
            "image": "Eddard_Stark.png"
        },
        "Eddard II": {
            "content": "Eddard II:En route to King's Landing, Eddard and Robert discuss Jon Snow’s mother, Daenerys’s wedding, and the appointment of Jaime Lannister as Warden of the East in place of Jon Arryn’s son, Robert.",
            "image": "Eddard_Stark.png"
        },
        "Eddard III": {
            "content": "Eddard III:Arya is brought before the king. Cersei demands that Arya and her wolf be punished for hurting the prince, but Nymeria has run off so the queen settles for Sansa’s direwolf, Lady, instead. Eddard kills Lady himself.",
            "image": "Eddard_Stark.png"
        },
        "Eddard IV": {
            "content": "Eddard IV:Eddard arrives in King s Landing and is shocked to learn that the king wants a tournament held in his honor. Littlefinger takes Eddard to see Catelyn.",
            "image": "Eddard_Stark.png"
        },
        "Eddard V": {
            "content": "Eddard V:Eddard interviews Grand Maester Pycelle about the death of Jon Arryn. Littlefinger informs Eddard about people who might have additional information, including Jon Arryn’s squire.",
            "image": "Eddard_Stark.png"
        },
        "Eddard VI": {
            "content": "Eddard VI:Eddard s investigation leads him to Gendry, a boy apprenticed to an armorer. Jon Arryn and Stannis Baratheon had previously visited the boy, who, as Eddard discovers, is an unwitting bastard of King Robert.",
            "image": "Eddard_Stark.png"
        },
        "Eddard VII": {
            "content": "Eddard VII:Eddard discusses the king s order to kill Daenerys with the small council. Varys reveals that Cersei intended to have Robert murdered during the event in an 'accident,' and also confirms that Jon Arryn was poisoned by the knight who died the previous day.",
            "image": "Eddard_Stark.png"
        },
        "Eddard VIII": {
            "content": "Eddard VIII:Robert learns that Daenerys is pregnant and orders her killed. Eddard resigns as Hand in protest.",
            "image": "Eddard_Stark.png"
        },
        "Eddard IX": {
            "content": "Eddard IX:Eddard discovers another bastard of Robert s at Chataya s brothel. Jaime accosts him in the street in anger over Tyrion s abduction. Jory is killed and Eddard breaks his leg.",
            "image": "Eddard_Stark.png"
        },
        "Eddard X": {
            "content": "Eddard X:Eddard dreams about fighting the last of the Kingsguard at the Tower of Joy. Robert and Eddard reconcile and Eddard is reinstated as Hand of the King.",
            "image": "Eddard_Stark.png"
        },
        "Eddard XI": {
            "content": "Eddard XI:Eddard hears testimony from Margaery Piper, Karyl Vance and Raymun Darry about a series of raids carried out by Gregor Clegane. Eddard attaints Gregor for treason and orders Lord Beric Dondarrion to bring him to justice.",
            "image": "Eddard_Stark.png"
        },
        "Eddard XII": {
            "content": "Eddard XII:Eddard meets with Cersei and reveals that he knows that Jaime is the father of her children. He warns her to go into exile before Robert returns from hunting.",
            "image": "Eddard_Stark.png"
        },
        "Eddard XIII": {
            "content": "Eddard XIII:Robert returns from his hunt mortally wounded and dictates his will, naming Eddard as Protector of the Realm. Eddard refuses Renly s offer to secure the royal children. Eddard writes a letter urging Stannis to take the Iron Throne.",
            "image": "Eddard_Stark.png"
        },
        "Eddard XIV": {
            "content": "Eddard XIV:Robert has died and Eddard presents his will to Cersei, who tears it up. Eddard declares Stannis the true king and orders the City Watch to arrest Cersei, but they apprehend him instead.",
            "image": "Eddard_Stark.png"
        },
        "Eddard XV": {
            "content": "Eddard XV:Varys comes to Eddard in the dungeons and tells him that if he confesses his 'crimes' he will be allowed to join the Night’s Watch.",
            "image": "Eddard_Stark.png"
        }
    }

    
    def display_Eddard(self, chapter_name):
        profile = self.show_Eddard_Chapter()
        chapter = profile[chapter_name]
        chapter_text = f"{chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(chapter['image'])
        
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
