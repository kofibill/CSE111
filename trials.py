import csv
from datetime import datetime


def main():

    key_index=0

    college=college_timetable('timetable.csv',key_index)

    name=input('Please enter our name:')
    edu_level=input('please enter your educational level: ')
    if edu_level=='college':
        print(name)
        print(college)

    else:
        print('none')
    print()
    date=datetime.now()
    print(date)

def college_timetable(filename, key_index_column):
    '''Read the contents of a csv file
       into a dictionary to produce a timetable 

       parameters:
       filename is the file to be read from
       key_column_index is will hold the key to the dictionary

       returns:a timetable dictionary
    '''
    dictionary={}
    with open(filename) as timetable:
        read=csv.reader(timetable)
        next(read)
        for time in read:
            key=time[key_index_column]
            dictionary[key]=time
    return dictionary

main()