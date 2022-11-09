import random
def one():
    try:
        size = int(input('size - '))
        begin = int(input('begin - '))
        end = int(input('end - '))
        my_list = list()
        my_list2 = list()
        for i in range(size):
            my_list.append(random.randint(begin, end))
        for i in range(size):
            my_list2.append(random.randint(begin, end))
        print(my_list, my_list2)



    except Exception as ex:
        print(f'Eror information: {ex}')


one()