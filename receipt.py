import csv
from datetime import datetime

def main():
        
    try:
        PRODUCT_NUMBER_INDEX= 0
        PRODUCT_NAME_INDEX= 1
        PRICE_INDEX= 2
    
        product_dict=read_dictionary('products.csv', PRODUCT_NUMBER_INDEX)
        #print(product_dict)
        print()
        print('William\'s Grocery store') #This is the name of the receipt
        print()
        
        
        QUANTITY_INDEX= 1
        with open('request.csv') as request_list:
            reader=csv.reader(request_list)
            next(reader)
            for request in reader:
                pronum=request[PRODUCT_NUMBER_INDEX]
                proname=product_dict[pronum][PRODUCT_NAME_INDEX]
                quantity=request[QUANTITY_INDEX]
                proprice=product_dict[pronum][PRICE_INDEX]
    
                print(f'{proname}: {quantity} @ {proprice}') #This line of code displays the product name, quantity and produt price.
    
            print()
            #This are the ordered list of items
            bread= 2
            yogurt_1= 4
            granola= 1
            twix_candy= 2
            yogurt_2 = 3
            num_of_items= bread + yogurt_1 + granola + twix_candy + yogurt_2
    
            # Calculation of the subtotal
            bread_sub=bread * 2.55
            yogurt_1_sub=yogurt_1 * 0.75
            granola_sub= granola * 3.21
            twix_candy_sub=twix_candy * 0.85
            yogurt_2_sub=yogurt_2 * 0.75
            sub_total=bread_sub + yogurt_1_sub + granola_sub + twix_candy_sub +yogurt_2_sub
    
            # Calculate for the sales tax
            sales_tax= 6/100
            
            # Calculate the total amount
            total= sub_total + sales_tax
    
            print(f'The total number of items are: {num_of_items}')#This displays the total number of items purchased.
            print(f'The subtotal is: {sub_total:.2f}')
            print(f'The sales tax is: {sales_tax}')
            print(f'The total is: {total:.2f}')
            print()
            print('Thank you for shopping at William\'s Grocery Store. Have a nice day!!')
            # Creativity
            print('Please complete a quick survey about your online shopping experience at William.Stores.com.')
            date=datetime.now()
            print(f'{date}')
    
    except FileNotFoundError as file_err:
        print(file_err)
        print(f'The filename doesnt exist. Please check your filename again. ')

    except PermissionError as per_err:
        print(per_err)
        print(f'You do not have the permission to open this file.')

    except KeyError as key_err:
        print(key_err)
        print(f'Unknown product ID found in request.csv file.')
        print('Please check your request.csv file again.')


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
    compound_dict={}
    with open(filename) as products_list:
        reader=csv.reader(products_list)
        next(reader)
        for products in reader:
            key=products[key_column_index]
            compound_dict[key]=products

    return compound_dict

if __name__ =="__main__":
    main()
