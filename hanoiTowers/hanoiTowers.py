def hanoi(di, o, a, d):
    if di == 1:
        print('Mover disco 1 de palo {} a palo {}'.format(o, d))
        return
    
    hanoi(di-1, o, d, a)
    print('Mover disco {} de palo {} a palo {}'.format(di, o, d))
    hanoi(di-1, a, o, d)

di = int(input('Inserte numero de discos: '))
hanoi(di, 'A', 'B', 'C')