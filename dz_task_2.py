# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающие словарь, где ключ - значение переданного аргумента,
# а значение - имя аргумента. Если ключ не хешируем, используйте его 
# строковое представление

def param_(**kwargs):
    keys2 = {}
    for key, value in kwargs.items():
        try:
            keys2[value] = key
        except:
            keys2[str(value)] = key
    return keys2

print(param_(first = 'Первый', second ='Второй', third ='Третий'))
