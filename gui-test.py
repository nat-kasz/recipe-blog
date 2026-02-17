
from nicegui import ui

ui.label('Hello NiceGUI!')

class Recipe:
    def __init__(self, name, ingredients, baking_instructions, photo=None):
        self.__name = name
        self.__ingredients = ingredients
        self.__baking_instructions = baking_instructions
        self.__photo = photo
        self.__matched_ingredients = {}
        for i in self.__ingredients:
            self.__matched_ingredients[i] = False

    def getname(self):
        return self.__name
    def getingredients(self):
        return self.__ingredients
    def getbaking_instructions(self):
        return self.__baking_instructions
    def getphoto(self):
        return self.__photo
    def get_matched_ingredients(self):
        return self.__matched_ingredients


r = Recipe('chlebek bananowy', {'banan': '2 sztuki', 'jajko': '3 sztuki', 'maka': '300 g'}, ['1. zmieszaj jajko z maka', '2. rozgniec banana'])
ingredients = r.getingredients()


ui.add_css('''
    .q-splitter__panel q-splitter__before {
        color: red;
        margin-left: 50px;
    }
''')



polish_alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

guessed = []
number_of_guesses = 0
word = ''

for index in range(0, len(polish_alphabet), 7):
    toggle1 = ui.toggle({1: polish_alphabet[index], 2: polish_alphabet[index+1], 3: polish_alphabet[index+2], 4: polish_alphabet[index+3], 5: polish_alphabet[index+4], 6: polish_alphabet[index+5], 7: polish_alphabet[index+6]})

for i in ingredients:
    word = i
    number_of_letters = len(word)
    with ui.row():
        for _ in range(number_of_letters):
            ui.label('_')


with ui.splitter().style('width: 15%;') as splitter:
    for i in ingredients:
        with splitter.before:
            ui.label(ingredients[i]).style('margin-left: 20px;')
        with splitter.after:
            if r.get_matched_ingredients()[i]:
                ui.label(i).style('margin-left: 20px;')


ui.run()