#  Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99
print(int (a))
print(int (b))

#  Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
site_name = 'www.my_site.com#about'
print(site_name.replace ('#','/'))

#  Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
word = 'stroka'
print(word + 'ing')

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = 'Ivanou Ivan'
new_name = name.split()
print(new_name[1] , new_name[0])

#  Напишите программу которая удаляет пробел в начале, в конце строки
word = '    Я выполняю домашнюю работу по Python     '
modified_word = word.strip()
print(modified_word)

#  Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {
    '1А': 25,
    '1Б': 23,
    '2А': 20,
    '2Б': 22,
    '3А': 24,
    '4А': 21,
    '5Б': 19,
    '6В': 26,
    '7А': 30,
    '8Г': 27
}
print(school)

# Создайте список и извлеките из него списка второй элемент
my_list = [1, 2, 3, 4, 5]
second_element = my_list[1]
print(second_element)

# Вывести входит ли строка1 в строку2 (пример: employ и employment)
word_one = 'employ'
word_two = 'employment'
b = word_two.find(word_one)
if b == 0:
    print('Строка1 входит в строку2')
else:
    print('Строка1 НЕ входит в строку2')


#Вывести нужные символы x = "My name is Agent Smith" print(x[?]) #y print(x[?:?:?]) #nesgt
x = 'My name is Agent Smith'
print(x[1])
print(x[3]+x[6]+x[9]+x[12]+x[-2])