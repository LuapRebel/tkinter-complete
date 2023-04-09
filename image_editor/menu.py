import customtkinter as ctk
from panels import Panel, SliderPanel


class Menu(ctk.CTkTabview):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        # widgets
        PositionFrame(self.tab("Position"), rotation, zoom)
        ColorFrame(self.tab("Color"))
        EffectsFrame(self.tab("Effects"))
        ExportFrame(self.tab("Export"))


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        SliderPanel(self, "Rotation", rotation, 0, 360)
        SliderPanel(self, "Zoom", zoom, 0, 200)


class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")


class EffectsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
