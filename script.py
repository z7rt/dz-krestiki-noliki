pole = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
def pole_viviod():
    print(pole[0], end=" ")
    print(pole[1], end=" ")
    print(pole[2])
    print(pole[3], end=" ")
    print(pole[4], end=" ")
    print(pole[5])
    print(pole[6], end=" ")
    print(pole[7], end=" ")
    print(pole[8])
def win():
    if pole[0] == "X" and pole[1] == "X" and pole[2] == "X":
        print('Победа за Х')
    if pole[3] == "X" and pole[4] == "X" and pole[5] == "X":
        print('Победа за Х')
    if pole[6] == "X" and pole[7] == "X" and pole[8] == "X":
        print('Победа за Х')
    if pole[0] == "X" and pole[3] == "X" and pole[6] == "X":
        print('Победа за Х')
    if pole[1] == "X" and pole[4] == "X" and pole[7] == "X":
        print('Победа за Х')
    if pole[2] == "X" and pole[5] == "X" and pole[8] == "X":
        print('Победа за Х')
    if pole[0] == "X" and pole[4] == "X" and pole[8] == "X":
        print('Победа за Х')
    if pole[2] == "X" and pole[4] == "X" and pole[6] == "X":
        print('Победа за Х')
    if pole[0] == "0" and pole[1] == "0" and pole[2] == "0":
        print('Победа за 0')
    if pole[3] == "0" and pole[4] == "0" and pole[5] == "0":
        print('Победа за 0')
    if pole[6] == "0" and pole[7] == "0" and pole[8] == "0":
        print('Победа за 0')
    if pole[0] == "0" and pole[3] == "0" and pole[6] == "0":
        print('Победа за 0')
    if pole[1] == "0" and pole[4] == "0" and pole[7] == "0":
        print('Победа за 0')
    if pole[2] == "0" and pole[5] == "0" and pole[8] == "0":
        print('Победа за 0')
    if pole[0] == "0" and pole[4] == "0" and pole[8] == "0":
        print('Победа за 0')
    if pole[2] == "0" and pole[4] == "0" and pole[6] == "0":
        print('Победа за 0')
def igra():
    pole[int(input('куда вы хотите поставить свой символ X?:')) - 1] = 'X'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ 0?:')) - 1] = '0'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ X?:')) - 1] = 'X'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ 0?:')) - 1] = '0'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ X?:')) - 1] = 'X'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ 0?:')) - 1] = '0'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ X?:')) - 1] = 'X'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ 0?:')) - 1] = '0'
    pole_viviod()
    win()
    pole[int(input('куда вы хотите поставить свой символ X?:')) - 1] = 'X'
    pole_viviod()
    win()
pole_viviod()
igra()

