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

print_abacus(0)
print_abacus(12345678)
print_abacus(1337)
print_abacus(4502)
print ('My Server Ram')
print_abacus(1024*16)


def isleapyear(year):
    if (year%4 == 0) and (year%400 == 0):
        return 1
    else:
        return 0 

def daysinmonth(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month in (2):
        a = isleapyear(year)
        if a == 1:
            return 29
        else:
            return 28
    else:
        return 'Invalid Month'

def daysbetweendates(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        return 'Invalid operation'
    else:
        if m1 > m2:
            return 'Invalid operation'
        else:
            if d1>d2:
                return 'Invalid operation'
            else:
                if y1 == y2:
                    if m1 == m2:
                        return d2-d1
                    else:
                        for i in range[m1:m2+1]:


                     
   
