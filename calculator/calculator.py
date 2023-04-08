import customtkinter as ctk
import darkdetect
from PIL import Image
from buttons import Button, ImageButton, MathButton, MathImageButton, NumButton
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

        # clear (AC) button
        Button(
            parent=self,
            func=self.clear,
            text=OPERATORS["clear"]["text"],
            col=OPERATORS["clear"]["col"],
            row=OPERATORS["clear"]["row"],
            font=main_font,
        )

        # % button
        Button(
            parent=self,
            func=self.percent,
            text=OPERATORS["percent"]["text"],
            col=OPERATORS["percent"]["col"],
            row=OPERATORS["percent"]["row"],
            font=main_font,
        )

        # +/- button
        # invert_image = ctk.CTkImage(light_image="", dark_image="")
        Button(
            parent=self,
            func=self.invert,
            text="+/-",
            col=OPERATORS["invert"]["col"],
            row=OPERATORS["invert"]["row"],
            font=main_font,
        )

        # number buttons
        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text=num,
                func=self.num_press,
                col=data["col"],
                row=data["row"],
                font=main_font,
                span=data["span"],
            )

        for operator, data in MATH_POSITIONS.items():
            if data["image_path"]:
                pass
                # divide_image = ctk.CTkImage(
                #     light_image=Image.open(data["image_path"]["dark"]),
                #     dark_image=Image.open(data["image_path"]["light"]),
                # )
                # MathImageButton(
                #     parent=self,
                #     operator=operator,
                #     func=self.math_press,
                #     col=data["col"],
                #     row=data["row"],
                #     image=divide_image,
                # )
            else:
                MathButton(
                    parent=self,
                    text=data["character"],
                    operator=operator,
                    func=self.math_press,
                    col=data["col"],
                    row=data["row"],
                    font=main_font,
                )

    def num_press(self, value):
        print(value)

    def math_press(self, value):
        print(value)

    def clear(self):
        print("clear")

    def percent(self):
        print("percent")

    def invert(self):
        print("invert")

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
