from user import User


def redirect_to_depiction_page(window, frame):
    frame.destroy()
    from pages.depiction_page import depiction_frame
    depiction_frame(window=window)


def redirect_to_menu(window, frame):
    frame.destroy()
    from pages.menu_page import menu_frame
    menu_frame(window)


def redirect_to_practice(window, frame):
    frame.destroy()
    User.question = 0
    from pages.practice_page import practice_frame
    practice_frame(window)
