from __future__ import annotations


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.funds = 0
        self.withdrawn = 0

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount: float, description=""):
        if amount > self.funds:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.withdrawn += amount
            self.funds -= amount
            return True

    def get_balance(self):
        return self.funds

    def transfer(self, amount: float, obj: Category):
        if self.withdraw(amount, description="Transfer to " + obj.name):
            obj.deposit(amount, description="Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount: float):
        if amount > self.funds:
            return False
        else:
            return True

    def __str__(self):

        output = self.name.center(30, "*") + "\n"
        for i in self.ledger:
            output += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + "\n"
        output += "Total: " + format(self.funds, ".2f")
        return output


def create_spend_chart(categories):
    names = []
    total_withdrawn = 0
    percentage = []
    for i in categories:
        total_withdrawn += i.withdrawn
    for i in categories:
        percentage.append((i.withdrawn / total_withdrawn) * 100)
    output = "Percentage spent by category\n"
    for n in range(100, -1, -10):
        output += f"{n:>3}| "
        for i in percentage:
            if i >= n:
                output += "o  "
            else:
                output += "   "
        output += "\n"
    output += f"    {(3*len(categories)+1)*'-'}\n"

    for cat in categories:
        names.append(cat.name)
    count = max(names, key=len)
    for i in range(len(count)):
        temp = "     "
        for j in names:
            if i >= len(j):
                temp += "   "
            else:
                temp += j[i] + "  "
        output += f"{temp}\n"
    output=output[:-1]
    return output

