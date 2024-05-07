
def multiplication_table(input_number):
    #Проверка на число
    try:
        input_number = int(input_number)
    except:
        print('Введенный текст не является числом или это не целое число')
        return 'err'
    
    numbers_list = []
    for number in range(1, input_number + 1): #Берём каждое число из диапазона от 0 до введённого числа
        multiplier_list = []
        for multiplier in range(1, 11): #Берём множтель из диапазона от 1 до 10
            multiplier_list.append(number * multiplier) #Умножаем и записываем в массив
        numbers_list.append([number, *multiplier_list]) #Добавляем в массив нумерацию

    for i in range(len(numbers_list)):
        print(*numbers_list[i]) #Выводим готовый массив с нумерацией

list_answer = multiplication_table(input("Введите цифру: "))
