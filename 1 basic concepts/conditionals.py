# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

a = 1
boss = False
if a > 5:
    print( '5 er besi')
    print('koto besi ke jane')
elif a > 3:
    print('olpo boro')
elif a == 2:
    print('ekdom dui er soman soman')
else:
    print('chooto  chooto raate lombi hoye')

# if boss is not True:
#     print('tel er bakso niye astesi boss re tell dio')
# else: 
#     print('lunch er pore asen')

if boss is not True:
    print('lunch er pore asen')
else: 
    print('tel er bakso niye astesi boss re tell dio')

coin = 'head'
# nested conditions
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do  something')
            if 8%2 == 0 and 5%2==1:
                print('even 8 is an even number')
else:
    print('you are loss not a boss')