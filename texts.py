class StartPage:
    hello_text = 'Hi! Welcome to MindSteps'
    name = 'What is your name?'


class EndDepictionPage:
    end_rule = ' , now you\nknow all about\nthis app'
    end_rule_lets = "Let's do some exercises!"


class BufferPage:
    well = "You're doing well!"


class MenuPage:
    choose = ' choose one\noption'


def get_depiction_third_text():
    with open('big_texts/depiction.txt', 'r') as file:
        return file.read()



class DepictionPage:
    depiction_first_text = '''MindSteps is an innovative app designed to help children enhance their 
    concentration and attention skills.
     It offers engaging activities that develop abilities in focusing and identifying 
     common characteristics among objects. 
     The playful format makes learning enjoyable, fostering better information retention and 
     increasing mental engagement.'''
    depiction_third_text = get_depiction_third_text()

