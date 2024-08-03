from datetime import datetime
import csv
import pandas as pd
from calculations import get_date, get_category, get_amount, get_description

class CSV():
    
    columns = ['date','category','amount','description']
    format = '%d-%m-%Y'

    @classmethod
    def initialize(cls):
        try:
            file = pd.read_csv('tracking.csv')
        except:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv('tracking.csv', columns=cls.columns,index=False)

    @classmethod
    def add_entry(cls, date, category, amount, description):
        data = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        with open('tracking.csv','a') as file:
            writer = csv.DictWriter(file,fieldnames=cls.columns)
            writer.writerow(data)
        print('Data added successfully')

    @classmethod
    def summarize(cls,start_date, end_date):
        start_date = datetime.strptime(start_date,cls.format)
        end_date = datetime.strptime(end_date,cls.format)
        if start_date > end_date:
            print('Start Date should less than End Date')
            return
        else:
            dateparse = lambda x: datetime.strptime(x, '%d-%m-%Y')
            df = pd.read_csv('tracking.csv', parse_dates=['date'], date_parser=dateparse)
            # df['date'] = pd.to_datetime(df['date'],format=cls.format)
            mask = (df['date'] >= start_date) & (df['date'] <= end_date)
            filtered_df = df.loc[mask]
            if filtered_df.empty:
                print(f'No transactions available in between {start_date.strftime(cls.format)} - {end_date.strftime(cls.format)}')
            else:
                print(f'\nTransaction from {start_date.strftime(cls.format)} to {end_date.strftime(cls.format)} :')
                print(filtered_df.to_string(index=False))
                total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
                total_expenses = filtered_df[filtered_df['category'] == 'Expenses']['amount'].sum()
                print('\n Summary:')
                print(f'Total Income : ${total_income:.2f}')
                print(f'Total Expenses : ${total_expenses:.2f}')
                print(f'Net Savings: ${(total_income-total_expenses):.2f}')


def add_data():
    CSV.initialize()
    date = get_date()
    category = get_category()
    amount = get_amount()
    description = get_description()
    CSV.add_entry(date, category, amount, description)

if __name__ == '__main__':
    while True:
        print('1. Adding a new transaction')
        print('2. View transaction and summary within a range')
        print('3. Exit')
        choice = int(input('Enter you choice :'))

        if choice == 1:
            add_data()
        elif choice == 2:
            start_date = input('Enter start date of transaction :')
            end_date = input('Enter end date of transaction :')
            CSV.summarize(start_date, end_date)
        elif choice == 3:
            print('Exiting...')
            break
        else:
            print('Invalid choice, Enter 1,2 and 3')
        
        


