##
#test = 1
####Цикл с предусловием
#while test < 6:
    
#    print(test)
#    test +=1
####Цикл с предусловием

#number = 0 
##while number <1000:
##    number+=1
#    if (number % 2 )!= 0:
#        continue
#    print("Четное число"+ str(number)) 
#Массивы
#tets =[1,2,3,[4,5,6]]
#print(tets[3][2])
#print(tets[3]*2)
#test = "Hello"
#i  = 1
#test1 =''
#while i < 5:
#    test1+=test[i]
#    i+=1
#print(test1)
#проверяет если в списке 4
#test = [1,2,3,4,5,6,7]
#if 4 in test: 
#    print('hello')

#проверяет,что нет 4 в списке
#test = [1,2,3,5,6,7]
#if 4 not in test: 
#    print('Bye')
#добавление элементов в список
#test = [1,2,3,5,6,7]
#test.append("hello")
#print(test)
#удаление элементов в списке
#test = [1,2,3,5,6,7]
##test.remove(1)
#rint(test)

#кол-во элементов в списке
#test = [1,2,3,5,6,7]
#print(len(test))

#добавление в нужную позицию (на пример 0)  в списке
#test = [1,2,3,5,6,7]
#test.insert(0,88)
#print(test)

#нахождение самого max элемента
#test = [1,2,3,5,6,7]

#print(max(test))

#нахождение самого min элемента
#test = [1,2,3,5,6,7]

#print(min(test))

#узнать кол-во дублей в списке (на пример 4)
#test = [1,2,3,5,6,7,4,4,4,4,4,4,4]

#print(test.count(4))

#перевернуть список
#test = [1,2,3,5,6,7,4,4,4,4,4,4,4]
#test.reverse()
#print(test)

#получение списка из чисел с диапозоном 100
##num = list(range(101))
#print(num)

#получение списка из  чисел опред с диапозоном от 50 до 100
#num = list(range(50,101))
#print(num)

#получение списка из  чисел опред с диапозоном от 50 до 100 с шагом 2
#num = list(range(50,101,2))
#print(num)

#цикл for в списке
#test = [1,2,3,5,6,7,4,4,4,4,4,4,4]
#for a in test:
 #   print(a)

#цикл for на 7 раз
#for a in range(7):
#    print('ffsf')

#def f(x,y):
#    if x > y:
#        return x
#    elif y > x:
#        return y 
#print(f(5,8))

#        return x
#        return y 
#print(f.__doc__)
#import random
#for i in range(10):
#    print(random.randint(0,100))
#from math import * #из модуля random импортируй все
#num= 25
#print(int(sqrt(num)))

#print(pi)
#try:
#    print( 7 / 0 )
#except ZeroDivisionError:
#    print('На ноль делить нельзя')
#print("program end")
#try:
#    print( 7 / 0 )
#except ZeroDivisionError:
#    pass
#print("program end")
#try:
#    print( 5 / 3 ) 
#
#except (ZeroDivisionError,NameError,TypeError):
#    print('пойманно исключение')
#finally:
#    print("Конец поимки искл")
#print("program  end")
 
#pogoda = 'Плохая'
#if pogoda == 'Плохая':
#    raise TypeError('объяснение ошибки')
#try: 
#    print(7/0)
#except:
#    raise
#class haAhError(Exception):
#    pass 
#raise haAhError('oбъяснение ошибки')
#def exc(a):
#    assert a !='',"field empty"
#    print(str(a )+"!")
#a = input('ccc?')
#exc(a)
#filename = input('Укажите файл:')
#text = input('Какой текст поместить в файл: ')
#file = open(filename,'w')

#file.write(text)

#file.close()
#file = open('1.txt','a')
#file.write( 'test ')
#file.close()
#Программ для копирования
filename1 = input('Введите название  файла для бекапа: ')
filename2 = 'backup_'+ filename1
file1 = open(filename1,'rb')
file2 = open(filename2,'wb')

file2.write( file1.read() )

file1.close()
file2.close()

print('Бекап успешно завершен!')