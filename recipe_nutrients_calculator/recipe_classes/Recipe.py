from dataclasses import dataclass
from typing import Dict

from recipe_classes import Ingredients


@dataclass
class Recipe:
    recipe_name: str
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

    @property
    def macros(self) -> Dict[str, float]:
        """
        Returns the quantity of the 3 macro nutrients present in the recipe.

        Returns:
            Dict[str, float]: Macros quantities
        """
        return {
            'carbs': self.total_carbs,
            'fats': self.total_fats,
            'proteins': self.total_proteins
        }
