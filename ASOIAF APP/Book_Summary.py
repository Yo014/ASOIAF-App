import tkinter as tk
import customtkinter as ctk
from PIL import Image

class BookSummary_BookI():
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.resizable(width = False,height = False)
        ctk.CTkButton._click_animation_running = False
        ctk.CTkButton._hover_animation_running = False
        
        # Create Text Box
        self.text_box = ctk.CTkTextbox(root, wrap="word", width=500, height=300)
        self.text_box.place(x=27, y=230)

        # Initialize GUI components
        self.create_image()
        self.create_buttons()
        
        # Display Summary
        self.show_summaryBookI("A Game of Thrones")

    def create_image(self):
        """Add and display image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(150, 190))
        
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)  # Adjust placement
        self.image_label.image = photo

    def create_buttons(self):
        """Add Back button."""
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback, text_color="black",
            width=80, height=30, corner_radius=8
        )
        button_back.place(x=20, y=30)

    def get_summaryBookI(self):
        """Return book summary data."""
        return {
            "A Game of Thrones": {
                "Plot introduction": "A Game of Thrones is set in Westeros, a land with long seasons reminiscent of Medieval Europe. "
                                     "Fifteen years before the story, a civil war called Roberts Rebellion overthrew the Targaryen dynasty. "
                                     "Robert Baratheon became king after defeating Prince Rhaegar Targaryen and marrying Cersei Lannister to secure alliances. "
                                     "The Targaryen heirs, Viserys and Daenerys, fled overseas, while House Martell withdrew in protest over the deaths of Rhaegars family.",
                "Plot summary": "The story begins in 298 AC, following three main storylines. In the Seven Kingdoms, Eddard Stark, Lord of Winterfell, "
                                "becomes Hand of the King but uncovers that King Roberts children are illegitimate. After Roberts death, Eddard is betrayed "
                                "and executed by Joffrey, leading to a civil war called the War of the Five Kings. Robb Stark, Eddards son, is declared King "
                                "in the North, while other contenders rise for the throne.",
                "On the Wall": "At the Wall, Jon Snow joins the Nights Watch and learns of growing dangers beyond the Wall, including the Others and a rising "
                               "King-Beyond-the-Wall, Mance Rayder. Jon faces trials and doubts but remains committed to his duty as the Watch prepares for war.",
                "Across the Narrow Sea": "In the East, Daenerys Targaryen is married to Khal Drogo to reclaim her throne. She gains confidence and strength but "
                                          "loses Drogo and their unborn child. Using dragon eggs gifted to her, Daenerys hatches three dragons, becoming their mother "
                                          "and a key player in the fight for the throne."
            }
        }

    def show_summaryBookI(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        # Update text box with the book summary
        self.update_text_box(book_summary["Plot introduction"] + "\n\n" + book_summary["Plot summary"] + "\n\n" + book_summary["On the Wall"] + "\n\n" + book_summary["Across the Narrow Sea"])
        
    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete(1.0, "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")
        
    def getback(self):
        self.root.destroy()  # Close the current window (self.root.destroy)
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()


class BookSummary_BookII:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)
        ctk.set_appearance_mode("dark")

        self.root.resizable(width = False,height = False)
        ctk.CTkButton._click_animation_running = False
        # Create Components
        self.create_image()
        self.create_buttons()
        self.create_text_box()

        # Display Book Summary
        self.show_summary("A Clash of Kings")

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_Of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Back Button."""
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

    def create_text_box(self):
        """Create Text Box for Book Summary."""
        self.text_box = ctk.CTkTextbox(
            self.root, wrap=tk.WORD, width=500, height=300, corner_radius=10, font=("Arial", 12)
        )
        self.text_box.place(x=27, y=230)
        self.text_box.configure(state="disabled")

    def get_summary(self):
        """Return Summary for 'A Clash of Kings'."""
        return {
            "A Clash of Kings": {
                "Plot summary": "A Clash of Kings continues the story after A Game of Thrones, with the Seven Kingdoms torn apart by civil war. Several contenders vie for the Iron Throne, including Stannis and Renly Baratheon, while Joffrey holds power in King's Landing with Lannister support. The conflict intensifies when Renly is mysteriously killed by a shadow creature summoned by Melisandre, a priestess serving Stannis. Meanwhile, the Greyjoys launch an attack on the North, with Theon Greyjoy capturing Winterfell before being betrayed and captured himself.",
                "In the Seven Kingdoms": "In King's Landing, Tyrion Lannister serves as Hand of the King and proves instrumental in defending the city against Stannis's assault during the Battle of the Blackwater. The city is saved through Tyrion's strategic use of wildfire and the timely arrival of Tyrell forces. While Robb Stark achieves victories in the Westerlands, he struggles to maintain control of the North due to the Greyjoy invasion.",
                "On the Wall": "Beyond the Wall, the Night's Watch embarks on a reconnaissance mission to investigate increasing wildling activity. Jon Snow, as part of a scouting party, is forced to infiltrate the wildlings by pretending to defect. They discover that Mance Rayder has assembled a massive wildling army threatening the Seven Kingdoms.",
                "Across the Narrow Sea": "In the eastern continent, Daenerys Targaryen leads her diminished following across the harsh red waste to reach Qarth. Although her dragons are growing, she fails to secure support for her claim to the Iron Throne. After a significant confrontation at the House of the Undying, where her dragon Drogon destroys the warlocks' temple, and surviving an assassination attempt, she accepts an offer to return to Pentos with agents of Illyrio Mopatis. Throughout the novel, supernatural elements become more prominent, particularly through Melisandre's shadow magic and the growing power of Daenerys's dragons."
            }
        }

    def show_summary(self, book_title):
        """Show Summary for Selected Book."""
        summary = self.get_summary()[book_title]
        full_summary = "\n\n".join(summary.values())
        self.update_text_box(full_summary)

    def update_text_box(self, text):
        """Update Text Box with Provided Text."""
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, text)
        self.text_box.configure(state="disabled")

    def getback(self):
        """Navigate Back to Book Info Page."""
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()

class BookSummary_BookIII:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        ctk.set_appearance_mode("dark")
        self.root.resizable(width=False, height=False)

        # Create Components
        self.create_image()
        self.create_buttons()
        self.create_text_box()
        
        # Initialize GUI components
        self.show_summaryBookI("A Storm of Swords")

    def create_image(self):
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_of_Swords.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ctk.CTkImage(light_image=resized_image, size=(150, 190))
        
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)  # Adjust placement
        self.image_label.image = photo

    def create_buttons(self):
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback, width=80, height=30, 
            fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)
        
    def create_text_box(self):
        # Create Text Box for Book Summary.
        self.text_box = ctk.CTkTextbox(
            self.root, wrap="word", width=500, height=300, corner_radius=10, font=("Arial", 12)
        )
        self.text_box.place(x=27, y=230)
        self.text_box.configure(state="disabled") 

    def get_summaryBookI(self):
        return {
            "A Storm of Swords": {
                "Plot summary": "The novel follows three main storylines...",
                "In the Seven Kingdoms": "The Stark cause suffers devastating losses...",
                "On the Wall": "At the Wall, the Night's Watch faces an invasion...",
                "Across the Narrow Sea": "In the east, Daenerys Targaryen builds her power base...",
            }
        }

    def show_summaryBookI(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        
        # Update text box with the book summary
        self.update_text_box(
            book_summary["Plot summary"] + "\n\n" +
            book_summary["On the Wall"] + "\n\n" +
            book_summary["Across the Narrow Sea"]
        )

    def update_text_box(self, text):
        # Update the text box with the provided text.
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")
    
    def getback(self):
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookIII
        BookInfo_BookIII(new_root)
        new_root.mainloop()

class BookSummary_BookIV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        ctk.set_appearance_mode("dark")
        self.root.resizable(width=False, height=False)

        # Create Components
        self.create_image()
        self.create_buttons()
        self.create_text_box()
        self.show_summaryBookI("A Feast for Crows")

    def create_image(self):
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_For_Crows.png"
        image = Image.open(image_path)
        image = image.resize((150, 190))
        photo = ctk.CTkImage(light_image=image, size=(150, 190))
        
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)

    def create_buttons(self):
        # Add buttons to the interface
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback, width=80, height=30, 
            fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

    def create_text_box(self):
        # Create Text Box for Book Summary.
        self.text_box = ctk.CTkTextbox(
            self.root, wrap="word", width=500, height=300, corner_radius=10, font=("Arial", 12)
        )
        self.text_box.place(x=27, y=230)
        self.text_box.configure(state="disabled")

    def get_summaryBookI(self):
        """Return book summary data."""
        return {
            "A Feast for Crows": {
                "Plot introduction": "The War of the Five Kings seems to be winding down...",
                "Plot summary": "In the aftermath of war, Westeros struggles to recover...",
                "On the Wall": "Jon Snow commands the Night's Watch as threats loom...",
                "Across the Narrow Sea": "Daenerys consolidates power while facing new challenges..."
            }
        }

    def show_summaryBookI(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        # Update text box with the book summary
        self.update_text_box(
            book_summary["Plot introduction"] + "\n\n" +
            book_summary["Plot summary"] + "\n\n" +
            book_summary["On the Wall"] + "\n\n" +
            book_summary["Across the Narrow Sea"]
        )
        
    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")
        
    def getback(self):
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()

class BookSummary_BookV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        ctk.set_appearance_mode("dark")


        # Create components
        self.create_image()
        self.create_buttons()
        self.create_text_box()

        # Show summary for "A Dance with Dragons"
        self.show_summaryBook("A Dance with Dragons")

    def create_image(self):
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_With_Dragons.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(light_image=resized_image, size=(150, 190))

        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)

    def create_buttons(self):
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback, width=80, height=30,
            fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

    def create_text_box(self):
        self.text_box = ctk.CTkTextbox(
            self.root, wrap="word", width=500, height=300, corner_radius=10, font=("Arial", 12)
        )
        self.text_box.place(x=27, y=230)
        self.text_box.configure(state="disabled")

    def get_summaryBookI(self):
        return {
            "A Dance with Dragons": {
                "Plot summary": "The Seven Kingdoms remain fragmented as Daenerys struggles to rule in Meereen...",
                "In the Seven Kingdoms": "Cersei faces trials, Tyrion flees Westeros, and chaos spreads...",
                "On the Wall": "Jon Snow balances leadership challenges while preparing for the undead threat...",
                "Across the Narrow Sea": "Daenerys builds alliances but faces new dangers...",
            }
        }

    def show_summaryBook(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot summary"] + "\n\n"
        plot_summary += book_summary["In the Seven Kingdoms"] + "\n\n"
        plot_summary += book_summary["On the Wall"] + "\n\n"
        plot_summary += book_summary["Across the Narrow Sea"]
        self.update_text_box(plot_summary)

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")

    def getback(self):
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookV
        BookInfo_BookV(new_root)
        new_root.mainloop()