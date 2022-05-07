'''
Дан список.
Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Входные данные
Некоторое количество целых чисел, разделённых пробелами (всего не более 2⋅105 чисел).

Выходные данные
Выведите через пробел элементы, которые встречаются в списке только один раз,
в том порядке, в котором они встречаются в списке.
'''

a = '1 2 2 3 3 3 4 6 3 7 5'.split()
a = [int(el) for el in a]
one = []
more = set()

for el in a:
    print(a)
    if el not in one and el not in more:
        one.append(el)
        print('NOT', one, more)
    elif el not in more:
        print('in', one, more)
        more.add(el)
    print()
print()
for el in one:
    if el not in more:
        print(el, end=' ')
