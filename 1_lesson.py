#1
a = '657'
print(a)

b = 'hello!'
print(b)

name = input('who are you:')
print ('i am a', name)

#2
time = int(input('введите время в секундах:'))
hours = time // 3600
minutes = (time // 60) - hours * 60
secunds = time % 60
print(hours, ':' , minutes, ':' , secunds)


#3
n = int(input('введите число:'))
print(int(n) + int(n * 10 + n) + int(n * 100+ n * 10+ n))

#4
number = int(input('введите целое число от 10 до 99:'))
one = number // 10
two = number - one * 10
while number > 0:
    if one > two:
        print ('первое больше')
        break
    if one < two:
        print ('второе больше')
        break
    if one == two:
        print(one, 'равна', two)
        break

#5
revenue = float(input('введите значение выручки: '))
costs = float(input('введите значение издержки:'))
p = revenue-costs
print(p)
if p > 0:
    print(p / revenue)
else:
    print ('выручка ниже издержек')
hc = int(input('введите численность'))
print (hc)
hc_rev = hc / revenue
print (hc_rev)

#6
# не успела((

