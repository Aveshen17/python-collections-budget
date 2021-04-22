from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)

spending_categories=[]

iter(expense) for expense in spending_categories:
    spending_counter = collections.Counter()
    spending_categories=[spending_categories , expense.category]
