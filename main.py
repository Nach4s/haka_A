import tkinter as tk
from styles import center, Colors, Sizes
import pages



window = tk.Tk()
window.title('MindSteps')
window.iconbitmap("media/icon.jpeg")
window.geometry(f'{Sizes.window_WIDTH}x{Sizes.window_HEIGHT}')
window.configure(bg = Colors.main_color )
window.resizable(False, False)
center(window)

pages.main_frame(window)




window.mainloop()
