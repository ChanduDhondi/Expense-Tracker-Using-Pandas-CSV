import pandas as pd
from datetime import datetime
    
def get_date():
    format = '%d-%m-%Y'
    date = input('Enter Date (dd-mm-yyy):')
    if not date:
        return datetime.today().strftime(format)
    else:
        validate = datetime.strptime(date,format)
        return validate.strftime(format)
    

def get_category():
    category = input('Enter category (I for income or E for expenses)').upper()
    category_type = {'I':'Income', 'E':'Expenses'}
    if category in category_type:
        return category_type[category]
    else:
        print('Invalid category please enter I for Income or E for expenses :')
        return get_category()

def get_amount():
    amount = float(input('Enter Amount :'))
    amount = round(amount,2)
    try :
        if amount <= 0:
            print('Amount must be non-negative or non-zero')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_description():
    return input('Enter Description (optional) :')
