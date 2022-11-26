import random

def main():
    list = [0]*random.randint(10,50)
    list_second = []
    list_third = []
    list_reverse_order = []

    for i in range (len(list)):
        list[i] = random.randint(0,100)
    for i in range(len(list) - 1, -1, -1):
        list_reverse_order.append(list[i])
    for i in range (1,len(list),2):
        list_second.append(list[i])
    for i in range (2,len(list),3):
        list_third.append(list[i])

    print('Исходный список:\n',list)
    print('Cписок, заполненный числами в обратном порядке:\n',list_reverse_order)
    print('Cписок, заполненный каждым вторым элементом:\n',list_second)
    print('Cписок, заполненный каждым третьим элементом:\n',list_third)

main()
