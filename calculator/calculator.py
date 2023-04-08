import customtkinter as ctk
import darkdetect
from settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        system_theme = "dark" if is_dark else "light"
        ctk.set_appearance_mode(system_theme)
        super().__init__(fg_color=(WHITE, BLACK))
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False, False)
        self.title("")
        # self.iconbitmap('empty.ico')
        self.title_bar_color(is_dark)

        # grid layout
        self.rowconfigure(tuple(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(tuple(range(MAIN_COLUMNS)), weight=1, uniform="a")

        # data
        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        results_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        # create output labels
        OutputLabel(self, 0, "se", main_font, self.formula_string)
        OutputLabel(self, 1, "e", results_font, self.result_string)

    def title_bar_color(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = (
                TITLE_BAR_HEX_COLORS["dark"]
                if is_dark
                else TITLE_BAR_HEX_COLORS["light"]
            )
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, sticky, font, string_var):
        super().__init__(master=parent, textvariable=string_var, font=font)
        self.grid(
            column=0,
            columnspan=4,
            row=row,
            sticky=sticky,
            padx=10,
        )


if __name__ == "__main__":
    Calculator(True)