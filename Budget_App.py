class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

        

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0
        if self.ledger:
            for transactions in self.ledger:
                self.balance += transactions['amount']
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):    
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self):
        multiple = int((30-(len(self.name)))/2)
        body = f"{'*'*multiple}{self.name}{'*'*multiple}"
        if len(body) != 30:
            body += '*\n'
        else:
            body += '\n'

        for i in self.ledger:
            desc = i['description'][:23]
            amt = f"{i['amount']:.2f}"
            body += f"{desc:<23}{amt:>7}\n"           

        body += f"Total: {self.get_balance():.2f}"
        return body.strip()
                      
       
    def calculate_withdrawl(self):
        withdraw = 0
        for transactions in self.ledger:
            if transactions['amount'] < 0:
                withdraw += -transactions['amount']
        return withdraw



def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    total_spent = 0
    for category in categories:     #calculate total spent
        total_spent += category.calculate_withdrawl()
    
    percentages = []                #percentages list to iterate over

    for category in categories:
        if total_spent > 0:
            percentage = (((category.calculate_withdrawl()/total_spent)*100) // 10) * 10        #rounding down to nearest 10 by using base division //
        else:
            percentage = 0
        percentages.append(percentage)

    for y in range (100, -1, -10):     #creating y axis
        line = f"{y:3}| "
        for num in percentages:
            line += "o  " if num >= y else "   "
        output += line + '\n'
    output += "    " + "-"*(len(categories)*3 + 1) + '\n'
    
    max_len = max(len(item.name) for item in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            line += f"{category.name[i]}  " if i < len(category.name) else "   "
        if i < max_len - 1:
            output += line + '\n'
        else:
            output += line
    return output




# Examples to test
clothes = Category('clothes')
clothes.deposit(500, '123456789012345678901234')
clothes.withdraw(335)    
food = Category('food')
food.deposit(900, 'deposit')
food.withdraw(256, 'milk, cereal, eggs, bacon, bread')
car = Category('car')
car.deposit(500, 'sold')
#print(food.get_balance())    
print(create_spend_chart([food, clothes, car]))