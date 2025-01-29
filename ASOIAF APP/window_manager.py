import customtkinter as ctk
from PIL import Image, ImageTk
from ASOIAF_APP import MainMenuPage
from Book_Info import BookInfo_BookI, BookInfo_BookII, BookInfo_BookIII, BookInfo_BookIV, BookInfo_BookV
from Book_Summary import BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV
from POV_Characters import POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII
from Map import MapsofASOIAF
from Character_profile_viewer import CharacterProfileBookI
from Appendix import AppendixBookI
from Arya import AryaBookI, AryaBookII, AryaBookIII
from Bran import BranBookI
from Catelyn import CatelynBookI
from Eddard import EddardBookI
from Jon import JonBookI
from Sansa import SansaBookI
from Tyrion import TyrionBookI
from Daenerys import DaenerysBookI


class WindowManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASOIAF App")
        self.eval('tk::PlaceWindow . left')
        self.geometry("555x600")
        self.frames = {}
        self.create_frames()
        self.resizable(False, False)
        self.show_frame(MainMenuPage)

    def create_frames(self):
        """
        Creates and initializes frames for different pages in the application.
        This method iterates over a predefined list of page classes, instantiates each one,
        and stores the instance in the `self.frames` dictionary with the class name as the key.
        Each frame is then placed in a grid layout with row and column configuration.
        The frames created include:
        - MainMenuPage
        - BookInfo_BookI
        - ........
        The grid layout is configured to expand and contract with the window size.
        Returns:
            None
        """

        for F in (MainMenuPage, BookInfo_BookI, BookInfo_BookII, BookInfo_BookIII, BookInfo_BookIV, BookInfo_BookV,
                  BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV,
                  POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII, MapsofASOIAF, CharacterProfileBookI, AppendixBookI, AryaBookI, 
                  AryaBookII, AryaBookIII, BranBookI, CatelynBookI, EddardBookI, JonBookI, SansaBookI, TyrionBookI, DaenerysBookI):
            page_name = F.__name__
            frame = F( self, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, page_class):
        frame = self.frames[page_class.__name__]
        frame.tkraise()
        frame.update_idletasks()
    

if __name__ == "__main__":
    app = WindowManager()
    app.mainloop()
