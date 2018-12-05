#This program displays a budget analysis for a user

budget_amount = float(input('Enter your budget amount for the month: '))
any_expenses = 'y'
total_expenses = 0.0
while any_expenses == 'y':
    expenses = float(input('Enter an expense for the month: '))
    total_expenses += expenses
    any_expenses = input('Do you have more expenses?:' \
                         'enter y for yes and n for no ')
if total_expenses > budget_amount:
     print('\nPlease you have overspend your $',\
           budget_amount,' budget amount by $'\
           ,total_expenses-budget_amount,sep='')
elif budget_amount > total_expenses :
    print('\nPlease you have underspend your $',\
          budget_amount,' budget amount by '\
          ,budget_amount-total_expenses,sep='')
else:
    print('\nYou use exactly your $',budget_amount,' budget amount',sep='')
