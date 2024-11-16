import tkinter as tk
from styles import Colors, Font, Sizes
from texts import DepictionPage
from pages.end_depiction_page import end_depiction_frame


def end_depiction(frame, window, button):
    button.destroy()
    frame.destroy()
    end_depiction_frame(window)


def second_depiction_frame(frame, window, button):
    button.destroy()
    frame.destroy()
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=DepictionPage.depiction_third_text, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=30)

    next_button = tk.Button(window, font=Font.base_font, text='Next', width=9, bg=Colors.button_color, )
    next_button.configure(command=lambda: end_depiction(frame, window, next_button))
    next_button.place(x=Sizes.window_WIDTH - 230, y=Sizes.window_HEIGHT - 80)





def depiction_frame(window):

    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text=DepictionPage.depiction_first_text, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    next_button = tk.Button(window, font=Font.base_font, text='Next', width=9, bg=Colors.button_color, )
    next_button.configure(command=lambda: second_depiction_frame(frame, window, next_button))
    next_button.place(x=Sizes.window_WIDTH - 230, y=Sizes.window_HEIGHT - 80)


