from recipe_classes import Ingredients, Recipe

arroz = Ingredients('arroz', 500, 650, 11.9, 1.05, 143)
ovos_pata = Ingredients('ovos de pata', 225, 504, 27, 41.81, 3.06)
ovos_galinha = Ingredients('ovos de galinha', 200, 308, 25.2, 21.2, 2.24)
oleo_soja = Ingredients('óleo de soja', 52, 432, 0, 48, 0)

ingredientes = [arroz, oleo_soja, ovos_galinha, ovos_pata]
torta_arroz_ovos = Recipe(ingredientes)

print(torta_arroz_ovos.total_carbs)
