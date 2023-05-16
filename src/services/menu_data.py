from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, mode="r") as file:
            lista_pratos = csv.reader(file, delimiter=",", quotechar='"')
            # Usando o conceito de desempacotamento
            header, *data = lista_pratos

        self.dishes = set()

        dicionario = {}

        for dish, price, ingredient, recipe_amount in data:
            if dish not in dicionario:
                instancia_prato = Dish(dish, float(price))
                instancia_ingrediente = Ingredient(ingredient)
                instancia_prato.add_ingredient_dependency(
                    instancia_ingrediente, int(recipe_amount)
                )
                dicionario[dish] = instancia_prato
            else:
                instancia_ingrediente = Ingredient(ingredient)
                dicionario[dish].add_ingredient_dependency(
                    instancia_ingrediente, int(recipe_amount)
                )

        self.dishes = set(dicionario.values())
