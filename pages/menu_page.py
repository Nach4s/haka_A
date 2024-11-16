import tkinter as tk
from styles import Colors, Font, Sizes
from texts import MenuPage
from user import User
from pages.depiction_page import depiction_frame
from pages.redirect import redirect_to_practice



def open_depiction(frame, window):
    frame.destroy()
    depiction_frame(window)


def open_practice(frame, window):
    frame.destroy()
    depiction_frame(window)


def menu_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=User.name + MenuPage.choose, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    rule_button = tk.Button(frame, font=Font.base_font, text='Depiction', bg=Colors.button_color, width=9,
                            command=lambda: open_depiction(frame, window))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Practice', bg=Colors.button_color, width=9,
                                command=lambda: redirect_to_practice(window, frame))
    practice_button.pack(pady=30)

