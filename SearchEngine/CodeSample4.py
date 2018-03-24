################## Practice Unit ####################
#1. Abacus 

def print_abacus(value):
    l = 10 - len(str(value))
    string = '00000*****'
    x = str(value)
    for i in range(10):
        if l>i:
            print ('|'+string+'   |')
    for p in x:
        z = int(p)
        print ('|'+string[:10-z]+'   '+string[10-z:]+'|')

#print_abacus(0)
#print_abacus(12345678)
#print_abacus(1337)
#print_abacus(4502)
#print ('My Server Ram')
#print_abacus(1024*16)
print_abacus(88451+1438)