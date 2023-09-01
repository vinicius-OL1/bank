def cont (numconta):
    ant = []
    meta = 0
    primo = False
    meta = numconta//2
    while True :
        if numconta % meta  == 0 and meta != 1:
       
            primo = False
            return False
            
        elif meta  == 1:
            primo = True
            return True
            
        else:
            meta -= 1


            
