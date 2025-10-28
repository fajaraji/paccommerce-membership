# %% import library
from tabulate import tabulate
from math import sqrt

# create data
data = {
    "Sumbul": "Platinum",
    "Cahya": "Platinum",
    "Ana": "Gold"
}

benefit = {
    "Membership" : ["Platinum", "Gold", "Silver"],
    "Discount" : ["15%", "10%", "8%"],
    "Another Benefit" : ["Silver + Gold Benefit + Holiday Voucher + Cashback max. 30%", "Silver + Online Ride Voucher", "Food Voucher"]
}
table_benefit = tabulate(benefit, headers="keys")

requirement = {
    "Membership" : ["Platinum", "Gold", "Silver"],
    "Monthly Expense (IDR million)" : [8, 6, 5],
    "Monthly Income (IDR million)" : [15, 10, 7]
}
table_requirement = tabulate(requirement, headers="keys")

# %% create user class
class Member:    
    def __init__(self, username, monthly_expense, monthly_income):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        
    def show_benefit(self):
        print(f"Benefit Membership PacCommerce\n")
        print(table_benefit)

    def show_requirement(self):
        print(f"Requirements Membership PacCommerce\n")
        print(table_requirement)

    def predict_membership(self, monthly_expense, monthly_income):
        tiers = requirement["Membership"]
        expenses = requirement["Monthly Expense (IDR million)"]
        incomes = requirement["Monthly Income (IDR million)"]

        ref = {
            tiers[0]: (expenses[0], incomes[0]),
            tiers[1]: (expenses[1], incomes[1]),   
            tiers[2]: (expenses[2], incomes[2])
        }
        
        # predict membership using euclidean distance
        distance = {
            tier: sqrt((monthly_expense - exp)**2 + (monthly_income - inc)**2)
            for tier, (exp, inc) in ref.items()
        } 

        predicted_membership = min(distance, key=distance.get)
        data[self.username] = predicted_membership  # add new user to data
        print(f"You are eligible for: {predicted_membership} Membership")
        return predicted_membership


    def check_membership(self, username):
        membership = data.get(self.username)
        if membership is None:
            print("Username not found.")
            return
                  
        print(f"Username: {self.username}")
        print(f"Current Membership: {membership}\n")

        benefit_per_tier = {
            "Platinum": {
                "Membership" : ["Platinum"],
                "Discount" : ["15%"],
                "Another Benefit" : ["Silver + Gold Benefit + Holiday Voucher + Cashback max. 30%"]
            },
            "Gold": {
                "Membership" : ["Gold"],
                "Discount" : ["10%"],
                "Another Benefit" : ["Silver + Online Ride Voucher"]
            },
            "Silver": {
                "Membership" : ["Silver"],
                "Discount" : ["8%"],
                "Another Benefit" : ["Food Voucher"]
            },
        }

        table = benefit_per_tier.get(membership)
        if table is None:
            print("Membership does not exist.")
            return
        print(f"{membership} PacCommerce Benefit List\n")
        print(tabulate(table, headers="keys"))

    def calculate_price(self, membership, price_list):
        if membership == "Platinum":
            discount = 0.15
        elif membership == "Gold":
            discount = 0.10
        elif membership == "Silver":
            discount = 0.08
        else:
            discount = 0.0

        total_price = sum(price_list)
        discounted_price = total_price * (1 - discount)
        print(f"Total price after {int(discount*100)}% discount for {membership} membership: IDR {discounted_price:,.2f}")

# %% create member object (existing user)
member1 = Member("Sumbul", 9, 16)

# %% check the data
print(data)

# %% test case 1 - show benefit
member1.show_benefit()

# %% test case 2 - show requirement
member1.show_requirement()

# %% test case 3 - predict membership with monthly expense and income
member1.predict_membership(9, 12)

# %% test case 4 - check membership based on username
member1.check_membership("Sumbul")

# %% test case 5 - calculate price after discount based on membership
member1.calculate_price("Platinum", [150000, 200000, 400000])

# %% test case 6 - create member object (new user)
member2 = Member("Bambang", 3, 4)

# %% test case 7 - predict membership for new user with monthly expense and income
member2.predict_membership(3, 4)

# %% test case 8 - check membership for new user based on username
member2.check_membership("Bambang")

# %% test case 9 - calculate price after discount based on membership for new user
member2.calculate_price("Silver", [300_000, 150_000, 1_250_000, 15_000])

