from datetime import datetime

def main():
   day=get_days(1).capitalize()
   sub1=get_subject_1(1).capitalize()
   sub2=get_subject_2(1).capitalize()
   sub3=get_subject_3(1).capitalize()
   print()
   print('Study Timetable')
   print()
   print('Please fill in the study timetable with any subject of your choice!!')
   print()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')

   day=get_days(2).capitalize()
   sub1=get_subject_1(2).capitalize()
   sub2=get_subject_2(2).capitalize()
   sub3=get_subject_3(2).capitalize()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')

   day=get_days(3).capitalize()
   sub1=get_subject_1(3).capitalize()
   sub2=get_subject_2(3).capitalize()
   sub3=get_subject_3(3).capitalize()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')

   day=get_days(4).capitalize()
   sub1=get_subject_1(4).capitalize()
   sub2=get_subject_2(4).capitalize()
   sub3=get_subject_3(4).capitalize()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')

   day=get_days(5).capitalize()
   sub1=get_subject_1(5).capitalize()
   sub2=get_subject_2(5).capitalize()
   sub3=get_subject_3(5).capitalize()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')

   day=get_days(6).capitalize()
   sub1=get_subject_1(6).capitalize()
   sub2=get_subject_2(6).capitalize()
   sub3=get_subject_3(6).capitalize()
   print(f'{day}: {sub1}(8am-10am) {sub2}(3pm-5pm) {sub3}(9pm-10:30pm)')
   print()

   date=datetime.now()
   print(date)


# Blue print of the timetable 
# print(f'{Day}: {Subjet_One}, {Subject_two}, {Subject_three}')
# One function will handles the days of the week, another will handle subject_one
# another subject two and another subject three


def get_days(day):
    '''Get the days of the weeks
       parameters:
       days: the days of the week.
       returns: days of the week
    '''
    if day==1:
        days='monday'
    elif day==2:
        days='tuesday'
    elif day==3:
        days='wednesday'
    elif day==4:
        days='thursday'
    elif day==5:
        days='friday'
    elif day==6:
        days='saturday'
    return days

def get_subject_1(subject):
    '''Get the names of the subject
       parameters:
       subject: the names of the first subjects
       return: subjects of the first days
    '''

    if subject==1:
        sub='Subject name'
    elif subject==2:
        sub='Subject name'
    elif subject==3:
        sub='Subject name'
    elif subject==4:
        sub='Subject name'
    elif subject==5:
        sub='Subject name'
    elif subject==6:
        sub='Subject name'
    return sub

def get_subject_2(subject):
    '''Get the names of the subject
       parameters:
       subject: the names of the first subjects
       return: subjects of the first days
    '''
    if subject==1:
        sub='Subject name'
    elif subject==2:
        sub='Subject name'
    elif subject==3:
        sub='Subject name'
    elif subject==4:
        sub='Subject name'
    elif subject==5:
        sub='Subject name'
    elif subject==6:
        sub='Subject name'
    return sub

def get_subject_3(subject):
    '''Get the names of the subject
       parameters:
       subject: the names of the first subjects
       return: subjects of the first days
    '''
    if subject==1:
        sub='Subject name'
    elif subject==2:
        sub='Subject name'
    elif subject==3:
        sub='Subject name'
    elif subject==4:
        sub='Subject name'
    elif subject==5:
        sub='Subject name'
    elif subject==6:
        sub='Subject name'
    return sub

if __name__=="__main__":
    main()
