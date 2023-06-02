# Задача 1
# Приведем список покупок в магазине
 
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
 
# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом
#   b. Добавьте фрукты из списка fruits в конец списка shop_list
 
fruits = ['Яблоко', 'Апельсин', 'Клубника']
 
#   c. Удалите из списка shop_list картофель
#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 
# comment

#from pprint import pprint
#pprint(dir(shop_list))

shop_list.insert(shop_list.index("Рис"),"Рыба")
print(shop_list)

shop_list.extend(fruits)
print(shop_list)

shop_list.remove("Картофель")
print(shop_list)

print(shop_list.index("Хлеб") + 1)
