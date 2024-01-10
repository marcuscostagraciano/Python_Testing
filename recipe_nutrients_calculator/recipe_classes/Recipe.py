from dataclasses import dataclass
from recipe_classes import Ingredients


@dataclass
class Recipe:
    ingredients_list: list[Ingredients]

    @property
    def weight(self) -> float:
        return sum([ingredient.grams for
                    ingredient in self.ingredients_list])

    @property
    def total_calories(self) -> float:
        return sum([ingredient.calories for
                    ingredient in self.ingredients_list])

    @property
    def total_proteins(self) -> float:
        return sum([ingredient.proteins for
                    ingredient in self.ingredients_list])

    @property
    def total_fats(self) -> float:
        return sum([ingredient.fats for
                    ingredient in self.ingredients_list])

    @property
    def total_carbs(self) -> float:
        return sum([ingredient.carbs for
                    ingredient in self.ingredients_list])
