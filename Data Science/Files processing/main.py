import json
from pprint import pprint
import pandas as pd



import xml.etree.ElementTree as ET

new_root = ET.Element('menu')
dish_1 = ET.SubElement(new_root, 'dish')
dish_2 = ET.SubElement(new_root, 'dish')
# print(new_root.getchildren())
dish_1.set('name', 'Кура')
dish_1.text = 'Белок'
new_root_string = ET.tostring(new_root)
# with open("new_menu.xml", "wb") as f:
#     f.write(new_root_string)
ET.ElementTree(new_root).write('new_menu_good.xml', encoding="utf-8")

exit(1)
tree = ET.parse('menu.xml')
root = tree.getroot()

import xmljson
print(xmljson.parker.data(root))

parker_json = xmljson.parker.data(root)
back_to_xml = xmljson.parker.etree(parker_json)

df_index = ['name', 'price', 'weight', 'class']
df = pd.DataFrame(columns=df_index)

for elem in root:
    elements = [elem.get('name'), elem[0].text, elem[1].text, elem[2].text]
    df = df.append(pd.Series(elements, index=df_index), ignore_index=True)
print(df)

print(len(root[0]))
print(root[0][1])
for elem in root:
    for subelem in elem:
        print(elem.attrib['name'], subelem.tag, subelem.text)
    print()
exit(1)

data = pd.read_excel('Fig3-1.xls', header=None)
pd.set_option('display.max_columns', None)

data_file = pd.ExcelFile('./Fig3-1.xls')
data = pd.read_excel(data_file, header=None)

# with pd.ExcelFile('Fig3-1.xls') as xls:
#     data['Sheet1'] = pd.read_excel(xls, 'Sheet1', na_values=['NA'])
#     data['Sheet2'] = pd.read_excel(xls, 'Sheet2')

data = pd.read_excel('Fig3-1.xls', ['Sheet1', 'Sheet2'])

data = pd.read_excel('http://www.econ.yale.edu/~shiller/data/Fig3-1.xls', header=None)

data = pd.read_excel("nakladnaya.xls", header=None, skiprows=2)
# data.dropna(inplace=True)
# print(data)


writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
workbook = writer.book
worksheet = writer.sheets['table1']
money_fmt = workbook.add_format({'bold': True})
name_fmt = workbook.add_format({'color': 'red'})

worksheet.set_column('E:F', 20, money_fmt)
worksheet.set_column(1, 1, 20, name_fmt)
exit(1)
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