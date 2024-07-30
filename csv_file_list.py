import csv

def main():
    # Read the contents of the dentists.csv file
    # into a compound list.
    dentists_list = read_compound_list("dentists.csv")

    # Print the entire list.
    print(dentists_list)


def read_compound_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list. Each element in the
    compound list will be a small list that contains
    the values from one row of the CSV file.

    Parameter filename: the name of the CSV file to read
    Return: a list of lists that contain strings
    """
    # Create an empty list that will
    # store the data from the CSV file.
    compound_list=[]
    with open('dentists.csv') as dentist_list:
        reader=csv.reader(dentist_list)
        for dentist in reader:
            compound_list.append(dentist)
    
    return compound_list

if __name__ =="__main__":
    main()
