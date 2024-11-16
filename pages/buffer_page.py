import tkinter as tk

from pages import redirect
from styles import Colors, Font, Sizes
from texts import BufferPage



def buffer_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text=BufferPage.well, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)



    rule_button = tk.Button(frame, font=Font.base_font, text='Depiction', bg=Colors.button_color, width=12,
                            command=lambda: redirect.redirect_to_depiction_page(window, frame))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Menu', bg=Colors.button_color, width=12,
                                command=lambda: redirect.redirect_to_menu(window, frame))
    practice_button.pack(pady=30)
