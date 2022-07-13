import json
from pprint import pprint
import pandas as pd

# with open('recipes.json') as f:
#    recipes = json.load(f)
#    # pprint(recipes[])
#    for recipe in recipes:  # начинаем перебор всех рецептов
#        if recipe['id'] == 23629:  # если id текущего рецепта равен искомому
#            print(recipe)  # выводим на экран кухню, к которой относится блюдо
#            break
#
#    i = set()
#    for recipe in recipes:  # начинаем перебор всех рецептов
#        # if recipe['cuisine'] != 'italian':
#        #     continue
#        for j in recipe['ingredients']:
#         i.add(j)  # добавляем название типа кухни к множеству
#    print(len(i))
#
#    ingredients = i
#    food = {}  # создаём пустой словарь для хранения информации об ингредиентах
#    for item in ingredients:  # перебираем список ингредиентов
#        food[item] = 0  # добавляем в словарь ключ, соответствующий очередному ингредиенту
#    for recipe in recipes:  # перебираем список рецептов
#        for item in recipe['ingredients']:  # и список ингредиентов в каждом рецепте
#            food[item] += 1  # увеличиваем значение нужного ключа в словаре на 1
#    print(food)
#    c = 0
#    for i, v in food.items():
#        if v == 1:
#            c += 1
#    print(c)
#
#    import pandas as pd
#
#    df = pd.DataFrame(recipes)
#    print(df.head())
#
#
#    def find_item(cell):
#        if item in cell:
#            return 1
#        return 0
#
#
#    for item in ingredients:
#        df[item] = df['ingredients'].apply(find_item)
#    df['ingredients'] = df['ingredients'].apply(len)
#
# with open('recipes.json') as f:
#     recipes = json.load(f)
#
#     ingredients = set()
#     for recipe in recipes:  # начинаем перебор всех рецептов
#         for j in recipe['ingredients']:
#          ingredients.add(j)  # добавляем название типа кухни к множеству
#
#     df = pd.DataFrame(recipes)
#
#     def find_item(cell):
#         if item in cell:
#             return 1
#         return 0
#
#
#     for item in ingredients:
#         df[item] = df['ingredients'].apply(find_item)
#     df['ingredients'] = df['ingredients'].apply(len)
#
#     df.to_csv('recipes.csv', index=False)

df = pd.read_csv('recipes.csv')
ids = list(df.id)
print(ids)

df = pd.read_csv('recipes.csv')
ingredients = list(df.columns[3:])
print(ingredients)

def make_list(df):
    ret = []
    for j, i in enumerate(ingredients):
        # print(j, i, df[df.columns[j+3]] == 1)
        if df.iloc[0, j+3] == 1:
            ret.append(i)
    return ret

new_recipes = []

# print(make_list(df[df['id'] == 10259]))

for current_id in ids:
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0]
    current_ingredients = make_list(df[df['id'] == current_id])
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients}
    new_recipes.append(current_recipe)
print(new_recipes)

# print(df[df['id'] == 10259].iloc[0, 4])
with open("new_recipes.json", "w") as write_file:
    json.dump(new_recipes, write_file)