import random

size_1 = int(input('first size - '))
begin_1 = int(input('begin - '))
end_1 = int(input('end - '))

list1 = list()

for i in range(size_1):
    list1.append(random.randint(begin_1, end_1))

for i in range(0, len(list1)):
    print(f'{list1[i]}[{i}]', end=' ')
print()

size_2 = int(input('second size - '))
begin_2 = int(input('begin - '))
end_2 = int(input('end - '))

list2 = list()

for i in range(size_2):
    list2.append(random.randint(begin_2, end_2))

for i in range(0, len(list2)):
    print(f'{list2[i]}[{i}]', end=' ')
print()

mer = list1 + list2
print(f'Merged list: {mer}')

non_d = list(dict.fromkeys(mer))
print(f'List whithout duplicates = {non_d}')

dup = [x for n, x in enumerate(mer) if x in mer[:n]]
print (f'Duplicates = {dup}')

print(f'min - {(min(mer))}')
print(f'max - {(max(mer))}')

def non_duplicates(mer):
    mp = {}
    for i in mer:
        mp[i] = mp[i] + 1 if i in mp else 1
    return {i for i in mp.keys() if mp[i] == 1}

print (f'non duplicates - {non_duplicates(mer)}')
