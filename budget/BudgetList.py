from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')


class BudgetList:
    def BudgetList(self, budget):
        self.budget=budget
        self.sum_expenses=0
        self.expenses=[]
        self.sum_overages=0
        self.overages=[]

    def append(self, item):
        check=self.sum_expenses+item
        if check<self.budget:
            self.expenses.append(item)
            self.sum_expenses+=item

    def __len__(self):
        length = length(self.expenses)+length(self.overages)
        return length


def main()
    myBudgetList = BudgetList(1200)

    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print("The count of all expenses: " {str(__len__(myBudgetList))} )
