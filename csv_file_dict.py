import csv


def main():
    # Index of the phone number column
    # in the dentists.csv file.
    PHONE_INDEX = 2

    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

    # Print the dentists compound dictionary.
    print(dentists_dict)


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
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary={}
    with open('dentists.csv') as dentist_list:
        reader=csv.reader(dentist_list)
        next(reader)
        for dentist in reader:
            key=dentist[key_column_index]
            dictionary[key]=dentist
    return dictionary


if __name__=="__main__":
   main()