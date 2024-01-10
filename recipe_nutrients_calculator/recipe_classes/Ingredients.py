from dataclasses import dataclass


@dataclass
class Ingredients:
    ingredient_name: str
    grams: float
    calories: float
    proteins: float
    fats: float
    carbs: float
