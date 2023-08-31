def cont (numconta):
    ant = []
    meta = 0
    primo = False
    meta = numconta//2
    while True :
        print('meta')
        if numconta % meta  == 0 and meta != 1:
            print (meta)
            primo = False
            break
        elif meta  == 1:
            primo = True
            print ('numero primo')
            break
        else:
            meta -= 1
test = int (input('digite o numero da conta: '))
cont(test)

            
