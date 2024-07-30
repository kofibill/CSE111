import csv

def main():
    I_number_index=0
    name_index=1
    
    student_dict=read_dictionary('students.csv', I_number_index)
    inumber=input('Please enter an i number: ')
    if inumber in student_dict:
        key=student_dict[inumber]
        name=key[name_index]
        print(name)

    else:
        print('No such students')




def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary={}
    
    with open(filename) as students_list:
        reader=csv.reader(students_list)
        next(reader)
        for students in reader:
            key=students[key_column_index]
            dictionary[key]=students
    return dictionary


if __name__ =="__main__":
    main()