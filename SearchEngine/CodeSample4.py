################## Practice Unit ####################
#1. Abacus 

def print_abacus(value):
    l = 10 - len(str(value))
    string = '00000*****'
    x = str(value)
    for i in range(10):
        if l>i:
            print ('|00000*****   |')
    string[::-1]
    for p in x:
        z = int(p)
        rstring = string[:10-z]+'   '+string[10-z:]
        print ('|'+rstring+'|')

print_abacus(0)
print_abacus(12345678)
print_abacus(1337)
print_abacus(4502)