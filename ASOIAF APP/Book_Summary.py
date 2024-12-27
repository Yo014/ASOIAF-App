import tkinter as tk
from PIL import Image, ImageTk

class BookSummary_BookI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=67, height=22, state="disabled")
        self.text_box.place(x=7, y=230)
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        self.create_buttons()
        
        self.show_summaryBookI("A Game of Thrones")
    def create_buttons(self):
        button_back = tk.Button(self.root, text="Back", command=self.getback, bg="light blue", width=0, height=0, font=("Arial"), relief=tk.FLAT)
        button_back.place(x=20, y=30)
        
    def get_summaryBookI(self):
        return{
            "A Game of Thrones":{
                "Plot introduction":"A Game of Thrones is set in Westeros, a land with long seasons reminiscent of Medieval Europe. Fifteen years before the story, a civil war called Roberts Rebellion overthrew the Targaryen dynasty. Robert Baratheon became king after defeating Prince Rhaegar Targaryen and marrying Cersei Lannister to secure alliances. The Targaryen heirs, Viserys and Daenerys, fled overseas, while House Martell withdrew in protest over the deaths of Rhaegars family.",
                "Plot summary":"The story begins in 298 AC, following three main storylines. In the Seven Kingdoms, Eddard Stark, Lord of Winterfell, becomes Hand of the King but uncovers that King Roberts children are illegitimate. After Roberts death, Eddard is betrayed and executed by Joffrey, leading to a civil war called the War of the Five Kings. Robb Stark, Eddards son, is declared King in the North, while other contenders rise for the throne.",
                "On the Wall":"At the Wall, Jon Snow joins the Nights Watch and learns of growing dangers beyond the Wall, including the Others and a rising King-Beyond-the-Wall, Mance Rayder. Jon faces trials and doubts but remains committed to his duty as the Watch prepares for war.",
                "Across the Narrow Sea":"In the East, Daenerys Targaryen is married to Khal Drogo to reclaim her throne. She gains confidence and strength but loses Drogo and their unborn child. Using dragon eggs gifted to her, Daenerys hatches three dragons, becoming their mother and a key player in the fight for the throne.",            
            }
        }
    def show_summaryBookI(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot introduction"]
        plot_summary += "\n\n" + book_summary["Plot summary"]
        plot_summary += "\n\n" + book_summary["On the Wall"]
        plot_summary += "\n\n" + book_summary["Across the Narrow Sea"]
        self.update_text_box(plot_summary)
        

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
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()
        
class BookSummary_BookII:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=67, height=22, state="disabled")
        self.text_box.place(x=7, y=230)
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_Of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        self.create_buttons()
        
        self.show_summaryBookI("A Clash of Kings")
    def create_buttons(self):
        button_back = tk.Button(self.root, text="Back", command=self.getback, bg="light blue", width=0, height=0, font=("Arial"), relief=tk.FLAT)
        button_back.place(x=20, y=30)
        
    def get_summaryBookI(self):
        return{
            "A Clash of Kings":{
                "Plot summary":"A Clash of Kings continues the story after A Game of Thrones, with the Seven Kingdoms torn apart by civil war. Several contenders vie for the Iron Throne, including Stannis and Renly Baratheon, while Joffrey holds power in Kings Landing with Lannister support. The conflict intensifies when Renly is mysteriously killed by a shadow creature summoned by Melisandre, a priestess serving Stannis. Meanwhile, the Greyjoys launch an attack on the North, with Theon Greyjoy capturing Winterfell before being betrayed and captured himself.",
                "In the Seven Kingdoms":"In Kings Landing, Tyrion Lannister serves as Hand of the King and proves instrumental in defending the city against Stannis's assault during the Battle of the Blackwater. The city is saved through Tyrion's strategic use of wildfire and the timely arrival of Tyrell forces. While Robb Stark achieves victories in the westerlands, he struggles to maintain control of the North due to the Greyjoy invasion.",
                "On the Wall":"Beyond the Wall, the Night's Watch embarks on a reconnaissance mission to investigate increasing wildling activity. Jon Snow, as part of a scouting party, is forced to infiltrate the wildlings by pretending to defect. They discover that Mance Rayder has assembled a massive wildling army threatening the Seven Kingdoms.",
                "Across the Narrow Sea":"In the eastern continent, Daenerys Targaryen leads her diminished following across the harsh red waste to reach Qarth. Although her dragons are growing, she fails to secure support for her claim to the Iron Throne. After a significant confrontation at the House of the Undying, where her dragon Drogon destroys the warlocks' temple, and surviving an assassination attempt, she accepts an offer to return to Pentos with agents of Illyrio Mopatis. Throughout the novel, supernatural elements become more prominent, particularly through Melisandre's shadow magic and the growing power of Daenerys's dragons.",            
            }
        }
    def show_summaryBookI(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot summary"]
        plot_summary += "\n\n" + book_summary["In the Seven Kingdoms"]
        plot_summary += "\n\n" + book_summary["On the Wall"]
        plot_summary += "\n\n" + book_summary["Across the Narrow Sea"]
        self.update_text_box(plot_summary)
        

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
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()

class BookSummary_BookIII:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=67, height=22, state="disabled")
        self.text_box.place(x=7, y=230)
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_of_Swords.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        self.create_buttons()
        
        self.show_summaryBook("A Storm of Swords")
    def create_buttons(self):
        button_back = tk.Button(self.root, text="Back", command=self.getback, bg="light blue", width=0, height=0, font=("Arial"), relief=tk.FLAT)
        button_back.place(x=20, y=30)
        
    def get_summaryBookI(self):
        return{
            "A Storm of Swords":{
                "Plot summary":"The novel follows three main storylines that unfold in the aftermath of the War of the Five Kings. In the Seven Kingdoms, the Lannisters strengthen their hold on the Iron Throne through an alliance with House Tyrell, though their victory is marred by King Joffrey's assassination at his own wedding feast. Tyrion Lannister is falsely accused of the murder, and after a trial by combat ends with his champion's death, he escapes with help from his brother Jaime. During his escape, he kills his father Tywin.",
                "In the Seven Kingdoms":"The Stark cause suffers devastating losses. Robb Stark alienates his key allies, the Freys, by breaking his marriage pact. This leads to the infamous Red Wedding, where the Freys and Boltons betray and murder Robb and Catelyn Stark along with many of their bannermen. Meanwhile, Arya Stark continues her journey through the war-torn riverlands, eventually leaving Westeros for Braavos, while Sansa Stark escapes King's Landing with Littlefinger's help and witnesses her aunt Lysa's murder at his hands.",
                "On the Wall":"At the Wall, the Night's Watch faces an invasion of wildlings led by Mance Rayder, who is fleeing from the threat of the Others. Jon Snow infiltrates the wildlings but ultimately returns to defend the Wall. The Watch suffers heavy losses, including the death of Lord Commander Mormont in a mutiny, but eventually repels the wildling attack with the unexpected help of Stannis Baratheon's forces. Jon Snow is elected as the new Lord Commander of the Night's Watch.",
                "Across the Narrow Sea":"In the east, Daenerys Targaryen builds her power base by acquiring an army of Unsullied warriors from Astapor. She liberates the slave cities of Slaver's Bay, conquering Astapor, Yunkai, and finally Meereen. She discovers Ser Jorah's betrayal and banishes him, while accepting Ser Barristan Selmy's service after he reveals his true identity. Rather than pressing on to Westeros, she decides to remain in Meereen to learn how to rule effectively.",            
            }
        }
    def show_summaryBook(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot summary"]
        plot_summary += "\n\n" + book_summary["In the Seven Kingdoms"]
        plot_summary += "\n\n" + book_summary["On the Wall"]
        plot_summary += "\n\n" + book_summary["Across the Narrow Sea"]
        self.update_text_box(plot_summary)
        

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
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookIII
        BookInfo_BookIII(new_root)
        new_root.mainloop()

class BookSummary_BookIV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=67, height=22, state="disabled")
        self.text_box.place(x=7, y=230)
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_For_Crows.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        self.create_buttons()
        
        self.show_summaryBook("A Feast for Crows")
    def create_buttons(self):
        button_back = tk.Button(self.root, text="Back", command=self.getback, bg="light blue", width=0, height=0, font=("Arial"), relief=tk.FLAT)
        button_back.place(x=20, y=30)
        
    def get_summaryBookI(self):
        return{
            "A Feast for Crows":{
                "Plot summary":"",
                "In King's Landing":"",
                "In the narrow sea":"",
                "In the Crownlands and riverlands":"",
                "In the Vale":"",
                "In Oldtown":"",
                "In Braavos":"",
                "In Dorne":"",         
            }
        }
    def show_summaryBook(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot summary"]
        plot_summary += "\n\n" + book_summary["In King's Landing"]
        plot_summary += "\n\n" + book_summary["In the narrow sea"]
        plot_summary += "\n\n" + book_summary["In the Crownlands and riverlands"]
        plot_summary += "\n\n" + book_summary["In the Vale"]
        plot_summary += "\n\n" + book_summary["In Oldtown"]
        plot_summary += "\n\n" + book_summary["In Braavos"]
        plot_summary += "\n\n" + book_summary["In Dorne"]
        self.update_text_box(plot_summary)
        

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
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookIV
        BookInfo_BookIV(new_root)
        new_root.mainloop()

class BookSummary_BookV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Summary")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=67, height=22, state="disabled")
        self.text_box.place(x=7, y=230)
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_With_Dragons.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        self.create_buttons()
        
        self.show_summaryBook("A Dance with Dragons")
    def create_buttons(self):
        button_back = tk.Button(self.root, text="Back", command=self.getback, bg="light blue", width=0, height=0, font=("Arial"), relief=tk.FLAT)
        button_back.place(x=20, y=30)
        
    def get_summaryBookI(self):
        return{
            "A Dance with Dragons":{
                "Plot summary":"",
                "In the Seven Kingdoms":"",
                "On the Wall":"",
                "Across the Narrow Sea":"",            
            }
        }
    def show_summaryBook(self, book_title):
        summary = self.get_summaryBookI()
        book_summary = summary[book_title]
        plot_summary = book_summary["Plot summary"]
        plot_summary += "\n\n" + book_summary["In the Seven Kingdoms"]
        plot_summary += "\n\n" + book_summary["On the Wall"]
        plot_summary += "\n\n" + book_summary["Across the Narrow Sea"]
        self.update_text_box(plot_summary)
        

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
    
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookV
        BookInfo_BookV(new_root)
        new_root.mainloop()