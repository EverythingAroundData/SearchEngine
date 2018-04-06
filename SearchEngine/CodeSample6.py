# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(univ_info):
    sofstudents = []
    tfees = []
    flist = []
    for olist in univ_info:
        sofstudents.append(olist[1])
        tfees.append(olist[1]*olist[2])
    flist.append(sum(sofstudents))
    flist.append(sum(tfees))
    return flist

print (total_enrollment(usa_univs))
print (total_enrollment(udacious_univs))

## Lesson 11, 2nd last program, and Lesson 12, 6th and 7th program  