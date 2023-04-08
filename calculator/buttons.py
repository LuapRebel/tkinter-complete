from customtkinter import CTkButton
from settings import *


class Button(CTkButton):
    def __init__(self, parent, func, text, column, row, font, color="dark-gray"):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING["corner-radius"],
            font=font,
            fg_color=COLORS[color]["fg"],
            hover_color=COLORS[color]["hover"],
            bg_color=COLORS[color]["text"],
        )
        self.grid(
            column=column,
            row=row,
            sticky="nsew",
            padx=STYLING["gap"],
            pady=STYLING["gap"],
        )


class ImageButton(CTkButton):
    def __init__(self, parent, func, text, column, row, image, color="dark-gray"):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING["corner-radius"],
            image=image,
            fg_color=COLORS[color]["fg"],
            hover_color=COLORS[color]["hover"],
            bg_color=COLORS[color]["text"],
        )
        self.grid(
            column=column,
            row=row,
            sticky="nsew",
            padx=STYLING["gap"],
            pady=STYLING["gap"],
        )
