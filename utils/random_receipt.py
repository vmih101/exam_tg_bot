from data.config import RECEIPT_LINK
import requests


class Receipt():
    def __init__(self):
        self.r = requests.get(RECEIPT_LINK)
        self.data = self.r.json()

    def meal_name(self):
        self.name = ''
        for i in self.data['meals']:
            self.name = i['strMeal']

    def meal_instruction(self):
        self.instruction = ''
        for i in self.data['meals']:
            self.instruction = i['strInstructions']

    def ingredient_measure(self):
        ingredients = []
        measures = []
        self.ingredient_measure = {}
        for i in self.data['meals']:
            for x in i.keys():
                if 'strIngredient' in x and i.get(x) != '':
                    ingredients.append(i.get(x))
                elif 'strMeasure' in x and i.get(x) != '':
                    measures.append(i.get(x))
        self.ingredient_measure = dict(zip(ingredients, measures))


    def str_for_bot(self):
        str_for_bot = f"Название:  {self.name}\n\n"
        str_for_bot += f"Способ приготовления:\n  {self.instruction}\n\n"
        str_for_bot += 'Ингредиенты: \n\n'
        for i in self.ingredient_measure:
            str_for_bot += f"{i}: {self.ingredient_measure.get(i)}\n"
        return str_for_bot


receipt = Receipt()
receipt.meal_name()
receipt.meal_instruction()
receipt.ingredient_measure()


















