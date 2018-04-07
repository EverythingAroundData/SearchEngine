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
print_abacus(88451+1438)


#2. No. of Days between dates

def isleapyear(year):
    if (year%4 == 0):
        if year%100 != 0:
            return 1
        else:
            return 0
    else:
        return 0 

def daysinmonth(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        a = isleapyear(year)
        if a == 1:
            return 29
        else:
            return 28
    else:
        return 'Invalid Month'

#### Please report issue if you find any with the below function
def daysbetweendates(y1, m1, d1, y2, m2, d2):
    
    if y1>y2 and m1>m2 and d1>d2:
        return 'Invalid Dates'
    if y1==y2 and m1>m2:
        return 'Invalid Dates'
    if y1==y2 and m1==m2 and d1>d2:
        return 'Invalid Dates'
    if d1 > daysinmonth(m1, y1) or d2 > daysinmonth(m2, y2):
        return 'Invalid Dates'
    if y1==y2 and m1==m2 and d1<d2:
        return d2-d1
    dayslist = []
    if y1==y2 and m1<m2:
        if m2-m1==1:
            return (daysinmonth(m1, y1)-d1)+d2
        if m2-m1>1:
            totaldays = 0
            daysinrange = (daysinmonth(m1, y1)-d1)+d2

            for i in list(range(m2)[m1+1:m2:1]):
                totaldays = totaldays + daysinmonth(i, y1)
                
            return totaldays + daysinrange
    if y1<y2:
        ym1 = m1
        sdays = 0
        while (ym1<=12 and y1<y2) or (ym1<m2 and y1==y2):
            if ym1 == 12:
                sdays = daysinmonth(ym1, y1)
                dayslist.append(sdays)
                ym1 = 1
                y1 = y1+1
            if ym1<12:
                sdays = daysinmonth(ym1, y1)
                dayslist.append(sdays)
                ym1 = ym1 + 1               
        sdays = daysinmonth(m2, y2)
        dayslist.append(sdays)
        dayslist[0] = dayslist[0] - d1
        dayslist[-1] = d2
        return sum(dayslist)


print (daysbetweendates(2012,1,1,2012,2,28))
print (daysbetweendates(2012,1,1,2012,3,1))
print (daysbetweendates(2011,6,30,2012,6,30))
print (daysbetweendates(2011,1,1,2012,8,8))
print (daysbetweendates(1900,1,1,1999,12,31))

print (daysbetweendates(2012,12,15,2013,2,31))