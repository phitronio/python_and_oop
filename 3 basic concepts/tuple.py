def multiple():
    return 3, 4
# print(multiple())
things = 'pen','tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[3:6])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)

# things[0]='wagon'
# print(things)

items = ('book', 'monitor')

# ignore
print(len(things))
mega = ([2, 3,4], [6,8,9,5])
# print(type(mega))
print(mega[0])
mega[0][1]=666
print(mega)