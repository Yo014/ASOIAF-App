import customtkinter as ctk
from PIL import Image, ImageTk

class AryaBookI(ctk.CTkFrame):
    """
    A class to represent the GUI for Arya's chapters in Book I of ASOIAF.
    Attributes
    ----------
    root : ctk.CTk
        The root window of the GUI.
    image_label : ctk.CTkLabel
        Label to display images.
    text_box : ctk.CTkTextbox
        Textbox to display chapter text.
    slider : ctk.CTkSlider
        Slider to select chapters.
    Methods
    -------
    __init__(root):
        Initializes the GUI components and sets up the main window.
    create_slider():
        Creates and places the slider widget.
    slider_changed(value):
        Callback function for slider value change, updates the displayed chapter.
    convert_to_roman(nums):
        Converts an integer to a Roman numeral.
    create_buttons():
        Creates and places the back button.
    show_Arya_Chapters():
        Returns a dictionary of Arya's chapters with their images and texts.
    display_Arya(Arya_name):
        Displays the selected Arya chapter's text and image.
    update_text_box(text):
        Updates the text in the text box.
    update_image(image_name):
        Updates the image in the image label.
    getback():
        Destroys the current window and returns to the previous window.
    """
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self,font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()
        
    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
                from_=1, to=5, number_of_steps=4,
                command=self.slider_changed, 
                width=400, 
                progress_color="dark red",
                button_color="white",
                button_hover_color="white",
                height=30
                )
        self.slider.place(x=75, y=530)
        self.slider.set(1)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Arya {self.convert_to_roman(chapter_index)}"
        self.display_Arya(chapter_name)
        
    def convert_to_roman(self, nums):
        roman_numerals = ["I", "II", "III", "IV", "V"]
        return roman_numerals[nums - 1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey"
        )
        button_back.place(x=20, y=30)


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
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")



class AryaBookII(ctk.CTkFrame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self,font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()
        
    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
        from_=1, to=10, number_of_steps=9,
        command=self.slider_changed, 
        width=400, 
        progress_color="dark red",
        button_color="white",
        button_hover_color="white",
        height=30
        )
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Arya {self.convert_to_roman(chapter_index)}"
        self.display_Arya(chapter_name) 

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        return roman_numerals[num - 1]

    def create_buttons(self):
        from ASOIAF_APP import MainMenuPage
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(MainMenuPage), width=80, height=30, 
            corner_radius=8
        )
        button_back.place(x=20, y=30)
    def show_Arya_Chapters(self):
        return {
            "Arya I": {
                "image": "Arya_Stark.png",
                "text": "Arya I: Arya travels north with Yoren and a bunch of recruits bound for the Wall."
                },
            "Arya II": {
                "image": "Arya_Stark.png",
                "text": "Arya II:Yoren's group is accosted by gold cloaks looking for Gendry."
                },
            "Arya III": {
                "image": "Arya_Stark.png",
                "text": "Arya III:Yoren takes his party off the kingsroad in an effort to avoid pursuit "
                },
            "Arya IV": {
                "image": "Arya_Stark.png",
                "text": "Arya IV:Yoren's party is attacked at an abandoned holdfast by Ser Amory Lorch. Arya escapes through a tunnel under the barn."
                },    
            "Arya V": {
                "image": "Arya_Stark.png",
                "text": "Arya V:Arya, Gendry and Hot Pie are captured by Gregor Clegane."
                },
            "Arya VI": {
                "image": "Arya_Stark.png",
                "text": "Arya VI:Arya is brought to Harrenhal, where she is made a servant."
                },
            "Arya VII": {
                "image": "Arya_Stark.png",
                "text": "Arya VII:Jaqen H'ghar promises to kill three men of Arya's choosing in return for saving his life."
                },
            "Arya VIII": {
                "image": "Arya_Stark.png",
                "text": "Arya VIII:Lord Tywin marches from Harrenhal. Arya has Jaqen kill Weese."
                },
            "Arya IX": {
                "image": "Arya_Stark.png",
                "text": "Arya IX:Arya enlists Jaqen's help in rescuing a group of newly-arrived northmen captives, who it turns out allowed themselves to be captured on purpose in order to take the castle. Roose Bolton arrives and takes charge of Harrenhal."
                },
            "Arya X": {
                "image": "Arya_Stark.png",
                "text": "Arya X:Arya, Gendry, and Hot Pie leave Harrenhal after Arya learns that Lord Roose means to give the castle to Vargo Hoat."},
              
        }
    
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
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")


class AryaBookIII(ctk.CTkFrame):
    """
    A class to represent the GUI for Arya's chapters in Book III of ASOIAF.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self,
            from_=1, to=13, number_of_steps=12,
            command=self.slider_changed,
            width=400,
            progress_color="dark red",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.place(x=75, y=530)
        self.slider.set(1)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Arya {self.convert_to_roman(chapter_index)}"
        self.display_Arya(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = [
            "I", "II", "III", "IV", "V", "VI", "VII",
            "VIII", "IX", "X", "XI", "XII", "XIII"
        ]
        return roman_numerals[num - 1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookIII
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookIII),
            width=80, height=30, corner_radius=8,
            bg_color="transparent", fg_color="transparent", hover_color="grey"
        )
        button_back.place(x=20, y=30)

    def show_Arya_Chapters(self):
        return {
            "Arya I": {
                "image": "Arya_Stark.png",
                "text": "Arya I: Arya, Gendry, and Hot Pie travel north from Harrenhal."
            },
            "Arya II": {
                "image": "Arya_Stark.png",
                "text": "Arya II: Arya, Gendry, and Hot Pie are captured by the Brotherhood Without Banners. Harwin recognizes her and reveals her identity."
            },
            "Arya III": {
                "image": "Arya_Stark.png",
                "text": "Arya III: The group of outlaws escort Arya, Hot Pie, and Gendry through the Riverlands looking for Lord Beric Dondarrion."
            },
            "Arya IV": {
                "image": "Arya_Stark.png",
                "text": "Arya IV: Greenbeard and his men continue their search for Lord Beric."
            },
            "Arya V": {
                "image": "Arya_Stark.png",
                "text": "Arya V: The outlaws come to Stoney Sept hunting for Lord Beric. The Mad Huntsman captures Sandor Clegane."
            },
            "Arya VI": {
                "image": "Arya_Stark.png",
                "text": "Arya VI: Arya and Sandor are brought before Lord Beric. Sandor kills Beric in a trial by combat, but Beric returns alive minutes later."
            },
            "Arya VII": {
                "image": "Arya_Stark.png",
                "text": "Arya VII: Lord Beric ambushes a group of Brave Companions."
            },
            "Arya VIII": {
                "image": "Arya_Stark.png",
                "text": "Arya VIII: Arya runs from the Brotherhood and gets captured by Sandor."
            },
            "Arya IX": {
                "image": "Arya_Stark.png",
                "text": "Arya IX: Sandor takes Arya towards the Twins so he can ransom her to Robb."
            },
            "Arya X": {
                "image": "Arya_Stark.png",
                "text": "Arya X: Sandor and Arya arrive at the Twins."
            },
            "Arya XI": {
                "image": "Arya_Stark.png",
                "text": "Arya XI: Arya and Sandor approach the Twins as the slaughter begins. Sandor prevents Arya from running into the castle."
            },
            "Arya XII": {
                "image": "Arya_Stark.png",
                "text": "Arya XII: Arya and Sandor travel towards the Eyrie, then Riverrun."
            },
            "Arya XIII": {
                "image": "Arya_Stark.png",
                "text": "Arya XIII: Sandor fights with Gregor’s men and is wounded. Arya leaves him and takes passage with a Braavosi ship using Jaqen’s coin."
            }
        }

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
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")


class AryaBookIV(ctk.CTkFrame):
    """
    A class to represent the GUI for Arya's chapters in Book IV of ASOIAF.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self,
            from_=1, to=3, number_of_steps=2,
            command=self.slider_changed,
            width=400,
            progress_color="dark red",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.place(x=75, y=530)
        self.slider.set(1)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = self.convert_to_label(chapter_index)
        self.display_Arya(chapter_name)

    def convert_to_label(self, index):
        labels = ["Arya I", "Arya II", "Cat Of The Canals"]
        return labels[index - 1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookIV
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookIV),
            width=80, height=30, corner_radius=8,
            bg_color="transparent", fg_color="transparent", hover_color="grey"
        )
        button_back.place(x=20, y=30)

    def show_Arya_Chapters(self):
        return {
            "Arya I": {
                "image": "Arya_Stark.png",
                "text": "Arya I: Arya arrives at Braavos and is accepted as a servant of the Many-Faced God."
            },
            "Arya II": {
                "image": "Arya_Stark.png",
                "text": "Arya II: Arya is accepted as an acolyte of the Many-Faced God and begins training. She learns Braavosi and is sent into the city to sell shellfish for Brusco."
            },
            "Cat Of The Canals": {
                "image": "Arya_Stark.png",
                "text": "Cat Of The Canals: Arya sells clams for Brusco and kills Dareon, a deserter. She tells the Kindly Man, who gives her milk, and she wakes up blind the next day."
            }
        }

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
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")


class AryaBookV(ctk.CTkFrame):
    """
    A class to represent the GUI for Arya's chapters in Book V of ASOIAF.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self,
            from_=1, to=2, number_of_steps=1,
            command=self.slider_changed,
            width=400,
            progress_color="dark red",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.place(x=75, y=530)
        self.slider.set(1)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = self.convert_to_label(chapter_index)
        self.display_Arya(chapter_name)

    def convert_to_label(self, index):
        labels = ["The Blind Girl", "The Ugly Little Girl"]
        return labels[index - 1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookV
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookV),
            width=80, height=30, corner_radius=8,
            bg_color="transparent", fg_color="transparent", hover_color="grey"
        )
        button_back.place(x=20, y=30)

    def show_Arya_Chapters(self):
        return {
            "The Blind Girl": {
                "image": "Arya_Stark.png",
                "text": "The Blind Girl: Arya develops new skills while training blind at the House of White and Black."
            },
            "The Ugly Little Girl": {
                "image": "Arya_Stark.png",
                "text": "The Ugly Little Girl: Arya accepts an assassination assignment and is given a new face."
            }
        }

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
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")
