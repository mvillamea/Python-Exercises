import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=''):
        """ appends an object to the ledger list """
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        """ appends an object as negative to the ledger list
            if there are enough funds and returns True if
            the withdraw was done and false otherwise"""
        state = True
        if not(self.check_funds(amount)):
            state = False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
        return state

    def get_balance(self):
        """eturns the current balance of the budget
        category based on the deposits and withdrawals
        that have occurred"""
        final_amount = 0
        for i in range(len(self.ledger)):
            final_amount += self.ledger[i]['amount']
        return final_amount

    def transfer(self, amount, budget_cat):
        """Adds a withdrawal with the amount and the description
        "Transfer to [Destination Budget Category]"and adds a deposit to the
        other budget category with the amount and the description
        "Transfer from [Source Budget Category]", if there are enough funds.
        Returns True if the transfer took place, and False otherwise."""
        state = True
        if not (self.check_funds(amount)):
            state = False
        else:
            self.withdraw(amount, 'Transfer to '+str(budget_cat.name))
            budget_cat.deposit(amount, 'Transfer from '+str(self.name))
        return state

    def check_funds(self, amount):
        """Returns False if the amount is greater than the balance of
        the budget category and returns True otherwise"""
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        """Returns the category in a ticket format"""
        number_stars = (30-len(self.name))//2
        title_line = '*'*number_stars+self.name+'*'*number_stars
        corpus = ''
        for i in range(len(self.ledger)):
            corpus += (((self.ledger[i])['description']))[0:min(23, len((self.ledger[i])['description']))].ljust(23)+(
                str("{:.2f}".format(round(float((self.ledger[i])['amount']), 2)))).rjust(7)+'\n'
            Total = 'Total: '+str("{:.2f}".format((round(float(self.get_balance()), 2))))
        return  title_line+'\n'+corpus+Total


def round_down(x):
    """Rounds down a number to the nearest 10"""
    return int(math.floor(x / 10.0)) * 10


def create_spend_chart(categories):
    """Creates a sort of bar chart with
    the percentages spent in each category"""
    graph = "Percentage spent by category\n"
    total_spendings = 0
    spendings = {}
    for category in categories:
        spendings[category.name] = 0
        for x in category.ledger:
            if x['amount'] < 0: #the withdraws are the ones with negative values
                spendings[category.name] += x['amount']
        spendings[category.name] = abs(spendings[category.name])
    for amount in spendings:
        total_spendings += spendings[amount]
    for amount in spendings:
        spendings[amount] = round_down(spendings[amount] / total_spendings * 100) #getting the percentage rounded down

    for i in range(100, -10, -10):
        """getting the main part of the graph"""
        graph += str(i).rjust(3) + '| '
        for category in categories:
            if spendings[category.name] >= i:
                graph += 'o  '
            else:
                graph += '   '
        graph += '\n'
    graph += '    ' + '-' * (1 + len(categories) * 3) + '\n'

    maxlen = 0
    for category in categories:
        if len(category.name) > maxlen:
            maxlen = len(category.name) # max string length between category names
    for i in range(maxlen):
        """getting the labels for the x-axis"""
        graph += '     '
        for category in categories:
            if len(category.name) > i:
                graph += category.name[i] + '  '
            else:
                graph += '   '
        graph += '\n '
    return graph[0:-1]







