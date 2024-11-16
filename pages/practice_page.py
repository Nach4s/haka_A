import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import pages.depiction_page
from styles import Colors, Font, Sizes
from texts import DepictionPage
from user import User
import random
from questions import questions, a
from pages.buffer_page import buffer_frame




def incorrect_answer(window, frame, index, questions):
    answer = messagebox.askyesno('Error', 'Try again')




def next_practice(frame, window, index, questions):
    try:
        frame.destroy()
    except:
        pass
    if index == len(questions):

        buffer_frame(window)
        return
    question = random.choice(questions)
    right_answer = question.right_answer
    answers = ['size', 'form', 'color']
    answers.remove(right_answer)
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()


    tk.Label(frame, text=f'{str(index + 1)}/{len(questions)}', font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=100)
    tk.Label(frame, text=question.question, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=100)

    first_button = tk.Button(frame, font=Font.base_font, text=right_answer, width=9, bg=Colors.button_color,
                             command=lambda: next_practice(frame, window, index + 1, questions))

    second_button = tk.Button(frame, font=Font.base_font, text=answers[0], width=9, bg=Colors.button_color,
                              command=lambda: incorrect_answer(window, frame, index, questions))

    third_button = tk.Button(frame, font=Font.base_font, text=answers[1], width=9, bg=Colors.button_color,
                             command=lambda: incorrect_answer(window, frame, index, questions))
    buttons = [first_button, second_button, third_button]
    random.shuffle(buttons)
    for btn in buttons:
        btn.pack(side=tk.LEFT, padx=30)


def practice_frame(window):

    random.shuffle(questions)

    question = random.choice(questions)
    right_answer = question.right_answer
    answers = ['size', 'form', 'color']
    answers.remove(right_answer)

    index = 0
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text=f'{str(index + 1)}/{len(questions)}', font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=100)
    tk.Label(frame, text=question.question, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=100)

    first_button = tk.Button(frame, font=Font.base_font, text=right_answer, width=9, bg=Colors.button_color,
                             command=lambda: next_practice(frame, window, index + 1, questions))

    second_button = tk.Button(frame, font=Font.base_font, text=answers[0], width=9, bg=Colors.button_color,
                              command=lambda: incorrect_answer(window, frame, index, questions))

    third_button = tk.Button(frame, font=Font.base_font, text=answers[1], width=9, bg=Colors.button_color,
                             command=lambda: incorrect_answer(window, frame, index, questions))
    buttons = [first_button, second_button, third_button]
    random.shuffle(buttons)
    for btn in buttons:
        btn.pack(side=tk.LEFT, padx=30)





