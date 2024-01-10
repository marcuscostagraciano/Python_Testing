from dataclasses import dataclass


@dataclass
class Ingredients:
    ingredient_name: str
    grams: float
    calories: float
    proteins: float
    fats: float
    carbs: float

    @property
    def calories_per_gram(self) -> float:
        return (self.calories / self.grams)

    @property
    def proteins_per_gram(self) -> float:
        return (self.proteins / self.grams)

    @property
    def fats_per_gram(self) -> float:
        return (self.fats / self.grams)

    @property
    def carbs_per_gram(self) -> float:
        return (self.carbs / self.grams)
