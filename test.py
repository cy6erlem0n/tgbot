#modul
import random

a = int(input("Enter num please !"))

def choiseAnswer (t):   

# list answer
    l = ["Вы ввели какую-то хуйню!!!"]
    lOne = ["Не вздумай ссать на улице, хуй отпадёт!!"]
    lTwo = ["Холодно пизда, лучше сиди в дотку покатай или вздрочни"]
    lThree = ["Шапку одень, еблан. Тоже мне, мамкин модник"]
    lFour = ["Куда в шортах долбоёб, хоть шапку надень"]
    lFive = ["Ммм, тёпленько уже, капюшон накинь уебан, а то последнее выдует"]
    lSix = ["Та сними ты уже блять этот пуховик, тепло же на улице кусок дерьма"]
    lSeven = ["Уух, топики, шортики, сиськи.. Охуенное время. КОНЧЕНЫЙ ты на баб смотри, а не в монитор свой ебучий"]
    lEight = ["Жара пиздец... Выжить можно только на пляже. Но какая тебе разница если ты из дома не вылазишь, пещерный гном"]
#choise if
    if t <= -30:
        l = lOne
    elif t <= -20 and  t > -30:
        l = lTwo       
    elif t <= -10 and  t > -20:
        l = lThree
    elif t <= 0 and  t > -10:
        l = lFour
    elif t > 0 and t < 10:
        l = lFive
    elif t > 10 and t < 20:
        l = lSix
    elif t > 20 and t < 30:
        l = lSeven
    elif t > 30:
        l = lEight
    i = random.randint(0,len(l))
    return l[i]
print(choiseAnswer(a))