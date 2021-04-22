from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)

spending_categories=[]
expense=iter(expenses.list)

for expense in expenses.list
    spending_counter = collections.Counter("spending_categories")
    spending_categories=[spending_categories , expense.category]

print(spending_counter)
