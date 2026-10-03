import json

def load_expense():
    try:
        with open("expense.json","r") as f:
            content=json.load(f)
            return content
        
    except FileNotFoundError:
        print("file not found")
        return []
    except json.JSONDecodeError:
        return []

def save_expense(content):
    with open("expense.json","w") as f:
        json.dump(content,f)

class Expense:
    def __init__(self,category,price,item):
        self.category=category
        self.price=price
        self.item=item
    def add_expense(self):
        content=load_expense()

        content.append({self.category:{"item":self.item,"price":self.price}})
        save_expense(content)
        print("expense added succesfully")

def show_all_expense():
    print(load_expense())

def show_total_spending():
    expense_list=load_expense()
    total=0
    for expense in expense_list:
        for value in expense.values():
            total+=value.get("price")
    print(f"total spending is {total}")

def show_spending_by_category(category):
    expense_list=load_expense()

    total=0
    for i in expense_list:
        if category in i :
            total += i[category]["price"]
    print(f"total {category} expense is {total}")

def delete_expense():
    category=input("Enter name of the category you wanna delete the expense of:")
    expense_list=load_expense()

    new_list = []

    for expense in expense_list:
        if category not in expense:
            new_list.append(expense)

    expense_list = new_list
    save_expense(expense_list)
    print("expense deleted successfully")

def highest_spending_category():
    expense_list=load_expense()
    new_dict={}
    for expense in expense_list:
        for category , details in expense.items():
            if category not in new_dict:
                new_dict[category]=0
            
            new_dict[category]+=details["price"]
    if not new_dict:
        print("No expenses found")
        return
    print(new_dict)
    sorted_list=sorted(new_dict.items(),key=lambda x:x[1],reverse=True)
    print( sorted_list[0])

def menu():
    while True:
        print("---menu---")
        print("1.add-expense")
        print("2.show-all-expense")
        print("3.show-total-spending")
        print("4.show-expence-by-category")
        print("5.delete-expense")
        print("6.highest_spending_category")
        print("7.exit")

        try:
            choice=int(input("enter your choice:"))
        except ValueError:
            print("Enter a valid choice")
            continue
        
        if(choice==1):
            try:
                category=input("enter your category:")
                item=input("Enter the name of the item:")
                price=int(input("enter price:"))
                e=Expense(category,price,item)
                e.add_expense()
            except ValueError:
                print("something went wrong")
        elif(choice==2):
            show_all_expense()
        elif(choice==3):
            show_total_spending()
        elif(choice==4):
            category=input("enter your category:")
            show_spending_by_category(category)
        elif(choice==5):
            delete_expense()
        elif(choice==6):
            highest_spending_category()
        elif(choice==7):
            break
        else:
            print("you have entered a invalid choice please try again")

menu()
