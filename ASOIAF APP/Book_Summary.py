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