
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

with ui.splitter().style('width: 100%;') as splitter:
    with splitter.before:
        with ui.grid(columns=7):
            index =0
            for i in range(0,5):
                for j in range(0,7):
                    ui.button(polish_alphabet[index])
                    index += 1
    with splitter.after:
        for i in ingredients:
            word = i
            number_of_letters = len(word)
            with ui.row().style('margin-left: 20px; font-size: 100px;'):
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