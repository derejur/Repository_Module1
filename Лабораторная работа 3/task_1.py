def find_index(items, target_item):
    try:
        return items.index(target_item)
    except ValueError:  # Вызываю исключение ValueError, если товар не найден
        return None  # Функция возращает None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # Вызоваю функцию, которая получает индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
