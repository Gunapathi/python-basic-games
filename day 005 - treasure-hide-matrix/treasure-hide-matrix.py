# import random
#
# random_int = random.randint(1, 10)
# print(random_int)
#
# random_float = random.random()
# print(random_float)

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input('Where do you want to put the tressure? Enter value sep by ","\n').split(',')
map[int(position[0])][int(position[1])] = 'X'
print(f"\n{row1}\n{row2}\n{row3}")