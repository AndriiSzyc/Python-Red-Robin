#1
int_a = 55
print('id int_a', id(int_a))
str_b = 'cursor'
print('ld str_b', id(str_b))
set_c = {1, 2, 3}
print('id set_c', id(set_c))
lst_d = [1, 2, 3]
print('id lst_d', id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('id dict_e', id(dict_e))

#2
lst_d.append(4)
lst_d.append(5)
print(lst_d)

lst_d = [1, 2, 3]
lst_d.extend([4, 5])
print(lst_d)

#3
print('type int_a', type(int_a))
print('type str_b', type(str_b))
print('type set_c', type(set_c))
print('type lst_d', type(lst_d))
print('type dict_e', type(dict_e))

#4
print('class int_a = int', isinstance(int_a, int))
print('class str_b = str', isinstance(str_b, str))
print('class set_c = set', isinstance(set_c, set))
print('class lst_d = list', isinstance(lst_d, list))
print('class dict_e = dict', isinstance(dict_e, dict))

#String formatting:
#5
print('Anna has {} apples and {} peaches'.format(5, 3))

#6
print('Anna has {1} apples and {0} peaches'.format(5, 3))

#7
print('Anna has {app} apples and {peach} peaches'.format(app =5, peach = 3))

#8
print('Anna has {app} apples and {peach} peaches'.format(app ='_' * 5, peach = '_' *3))

#9
app = 5
peach = 3
print(f'Anna has {app} apples and {peach} peaches')

#10
print('Anna has %s apples and %s peaches' % (app, peach))

#11
fruit = {'apples': 5, 'peaches': 3}
print('Anna has {} apples and {} peaches'.format(fruit['apples'], fruit['peaches']))

#Comprehensions:
#list comprehension
#12
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

list_comprehension = [num ** 2 if num % 2 == 1 else num**4 for num in range(10)]
print(list_comprehension)

#13
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

lst = []
for num in range(10):
    if num % 2 == 0:
        num = num//2
        lst.append(num)
    else:
        num = num*10
        lst.append(num)
print(lst)

#dict comprehension
#14
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

dict_comprehension = {num: num**2 for num in range(1,11) if num%2 == 1}
print(dict_comprehension)

#15
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

dict_comprehension = {num: num**2 if num % 2 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)

#16
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

dict ={}
for x in range(10):
    if x**3%4 ==0:
        dict[x] = x**3
print(dict)

#17
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

dict = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict[x] = x**3
    else:
        dict[x] = x
print(dict)

#Lambda:
#18
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(2, 3))

foo = lambda x, y: x if x < y else y
print(foo(2, 3))

#19
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(2, 5, 3))

def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(2, 5, 3))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

#20
print(sorted(lst_to_sort))

#21
print(sorted(lst_to_sort, reverse=True))

#22
lst_to_sort = list(map(lambda n: 2 * n, lst_to_sort))
print(lst_to_sort)

#23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_A = list(map(lambda n, m: n + (m - n), list_A, list_B ))
print(list_A)

list_A = [2, 3, 4]
list_B = [5, 6, 7]
count = 0
for i in list_A:
    num = list_B[count] - i
    list_A[count] = i + num
    count +=1
print(list_A)

#24
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort = list(filter(lambda n: n % 2 == 1, lst_to_sort) )
print(lst_to_sort)

#25
b = range(-10, 10)
lst_sort = list(filter(lambda n: n < 0, b))
print(lst_sort)

#26
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
lst_gen = list(filter(lambda n: n in list_2, list_1))
print(lst_gen)  
