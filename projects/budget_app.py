
class Category:

    def __init__(self, name):
        self.ledger = []
        self.balance = 0.00
        self.name = name

    def __str__(self):
        tl = 30
        rl = (tl-len(self.name))//2
        padding = tl-(rl*2)-len(self.name)
        string = f"{'*'*rl}{self.name}{'*'*(rl+padding)}\n"
        for s in self.ledger:
            remainingL = \
                tl - len(format(s['amount'], '.2f')[:7]+s['description'][:23])
            string += f"{s['description'][:23]}{' '*remainingL}{format(s['amount'], '.2f')[:7]}\n"
        string += f"Total: {self.balance}"
        return string

    def check_funds(self, amount):
        return (self.balance - amount) >= 0

    def deposit(self, amount, description=""):
        new_entry = {"amount": round(float(amount), 2),
                     "description": description}
        self.balance += amount
        self.ledger.append(new_entry)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        new_entry = {"amount": round(float(amount*-1), 2),
                     "description": description}
        self.balance -= amount
        self.ledger.append(new_entry)
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_category):
        if not self.check_funds(amount) and not self is target_category:
            return False

        def template(a, b): return f"Transfer {a} {b}"
        self.withdraw(amount, template("to", target_category.name))
        target_category.deposit(amount, template("from", self.name))
        return True


def create_spend_chart(arr):
    chart = {}
    total_spend = 0
    for obj in arr:
        chart[obj.name] = \
            sum([-1*entry['amount']
                for entry in obj.ledger if entry['amount'] < 0])
        total_spend += chart[obj.name]
    for cloumn in chart:
        chart[cloumn] = int(round(chart[cloumn]/total_spend * 100))
    string = 'Percentage spent by category\n'
    row_len = (3*len(arr))+5
    for i in range(100, -1, -10):
        plot = "  ".join(["o"if chart[j] >= i else " " for j in chart])
        row = f"{' '*(3-len(str(i)))}{str(i)}| {plot}  \n"
        string += row
    string += f"{' '*4}{'-'*(row_len -4)}\n"
    max_len = len(max(list(chart.keys()), key=lambda s: len(s)))
    for i in range(max_len):
        pre_str = "  ".join([n[i] if len(n) > i else " " for n in chart])
        row = f"{' '*5}{pre_str}  \n"
        string += row
    return string.rstrip('\n')
