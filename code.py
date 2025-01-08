from datetime import datetime
import pyfiglet as p

class BudgetTracker:
    def __init__(self,budget):
        self.budget=budget
        self.expenses=[]
        self.category_totals={}

    def add_expense(self,cat,desc,amt):
        self.expenses.append({"category": cat,"description": desc,"amount": amt,"date": datetime.now().date()})
        if cat in self.category_totals:
            self.category_totals[cat]+=amt
        else:
            self.category_totals[cat]=amt

    def get_total_spent(self):
        return sum(expense["amount"] for expense in self.expenses)

    def get_remaining_budget(self):
        return (self.budget-self.get_total_spent())

    def check_budget_status(self):
        remain=self.get_remaining_budget()
        if remain<=0:
            return "Budget exceeded!"
        elif remain<=0.1*self.budget:
            return "Warning: Budget almost exhausted!"
        return "Budget on track."

    def suggest_saving_areas(self):       
        high=max(self.category_totals, key=self.category_totals.get)
        return f"Consider reducing spending in '{high}' to save more."
    
    def display_expenses(self):
        print("\n------------------------ Expense Details ------------------------\n")
        for expense in self.expenses:
            cat=expense["category"]
            desc=expense["description"]
            amt=expense["amount"]
            date=expense["date"]
            print(f"Category: {cat}, Description: {desc}, Amount: ₹{amt}, Date: {date}")
        print("\n------------------------------------------------------------------\n")

    def reset_expenses(self):
        self.budget=0
        self.expenses=[]
        self.category_totals={}


def main():
    obj=BudgetTracker(0)
    print(p.figlet_format('Welcome to the Budget Tracker!'))
    while True:
        budget=int(input('Enter your budget: '))
        obj.budget=budget
        print(f"Your budget for this period is set to ₹{obj.budget}.")
        check=False
        while True:
            c=input('Wanna insert a expense?(Yes/No)').lower()
            if c=='yes':
                check=True
                cat=input('Enter expense category: ').upper()
                desc=input('Enter expense description: ').upper()
                amt=int(input('Enter expense amount: '))
                obj.add_expense(cat,desc,amt)
            else:
                break

        if check:
            print("\n----------------\nCategory Summary:\n----------------\n")
            for cat, total in obj.category_totals.items():
                print(f"  {cat}: ₹{total}")
            print('\n----------------')

            print(f"\nTotal Spent: ₹{obj.get_total_spent()}")
            
            print(f"\nRemaining Budget: ₹{obj.get_remaining_budget()}")

            print(f"\nBudget Status: {obj.check_budget_status()}")

            print(f"\nSaving Suggestion: {obj.suggest_saving_areas()}")

            d=input('Wanna see expense details?(Yes/No)').lower()
            if d=='yes':
                obj.display_expenses()
        
        r=input("\nWould you like to reset expenses & start a new period? (Yes/No): ").lower()
        if r=='yes':
            obj.reset_expenses()
            print("Expenses have been reset for the new period.")
        else:
            print('')
            print(p.figlet_format('Thanks for using!'))
            break

main()
