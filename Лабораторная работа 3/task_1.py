# TODO Напишите функцию для поиска индекса товара
def Find_item(item_list, item_name):
    for i in range(len(item_list)):
        if item_name == item_list[i]:
            return i

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = Find_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
