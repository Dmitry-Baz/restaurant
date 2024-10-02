cook_book = {
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    ],
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    ],
}

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list

# Пример использования
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)