class DepartmentReport():
    def __init__(self, company_name):
        self.revenues = []
        self.company_name = company_name

    def add_revenue(self, elem):
        self.revenues.append(elem)

    def average_revenue(self):
        return f'Average department revenue for {self.company_name}: {round(sum(self.revenues)/len(self.revenues))}'


report = DepartmentReport('123')
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
print(report.average_revenue())

class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance

    def login(self, email, password):
        return self.email ==email and self.password == password

    def update_balance(self, amount):
        self.balance += amount

    def add_revenue(self, elem):
        self.revenues.append(elem)

    def average_revenue(self):
        return f'Average department revenue for {self.company_name}: {round(sum(self.revenues)/len(self.revenues))}'

class IntDataFrame():
    def __init__(self, mlist):
        self.mlist = mlist

    def count(self):
        return len([int(i) for i in self.mlist if i >= 1])

    def unique(self):
        return len(set([int(i) for i in self.mlist]))
df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])
print(df.mlist)

class OwnLogger:
    def __init__(self):
        self.messages = []

    def log(self, message, level):
        self.messages.append((message, level))

    def show_last(self, level='all'):
        if level == 'all':
            return self.messages[-1][0]
        else:
            for message, lvl in reversed(self.messages):
                if lvl == level:
                    return message

class Dog():
    def bark(self):
        return 'Bark!'
    def give_paw(self):
        return 'Paw'