class Category:
    def __init__(self, category) -> None:
        self.category = category
        self.ledger = []

    def deposit(self, amount, desc="") -> None:
        temp = {"amount": amount, "description": desc}
        self.ledger.append(temp)

    def withdraw(self, amount, desc="") -> bool:
        temp = {"amount": amount * -1, "description": desc}
        if self.check_funds(amount):
            self.ledger.append(temp)
            return True
        return False

    def transfer(self, amount, category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        return False

    def check_funds(self, amount) -> bool:
        return False if amount > self.get_balance() else True

    def get_balance(self):
        nums = []
        for transaction in self.ledger:
            nums.append(transaction["amount"])
        return sum(nums)

    def __str__(self) -> str:
        resultString = '{:*^30s}\n'.format(self.category)
        for trans in self.ledger:
            resultString += '{:<23}{:>7.2f}\n'.format(
                trans["description"][:23], trans["amount"])
        resultString += "Total: {:.2f}".format(self.get_balance())
        return resultString


def create_spend_chart(categories) -> str:
    resultString = "Percentage spent by category\n"

    # obtain total spent for each category
    spentAmounts = dict()
    for category in categories:
        categorySpent = []
        for trans in category.ledger:
            if trans['amount'] < 0:
                categorySpent.append(trans['amount'])
        spentAmounts[category.category] = sum(categorySpent) * -1

    # obtain total spent
    totalSpent = 0
    for key, value in spentAmounts.items():
        totalSpent += value

    # obtain percentage spent values on each category
    for key, value in spentAmounts.items():
        spentAmounts[key] = (value / totalSpent) * 100

    # create the dict of percentages for the chart
    percentages = dict()
    for i in range(100, -1, -10):
        percentages['{:>3}|'.format(i)] = i

    # add chart characters to result string
    chartLine = ""
    for strPercent, percentValue in percentages.items():
        chartLine = strPercent
        for category, spent in spentAmounts.items():
            if spent >= percentValue:
                chartLine += " o "
            else:
                chartLine += "   "
        resultString += chartLine + " \n"

    # x axis line
    resultString += "    " + "---" * len(categories) + "-\n"

    # add the x axis labels
    longestWordLength = 0
    for category in spentAmounts:
        if len(category) > longestWordLength:
            longestWordLength = len(category)

    for i in range(longestWordLength):
        xLabel = "    "
        for category in spentAmounts:
            try:
                xLabel += " {} ".format(category[i])
            except:
                xLabel += "   "
        xLabel += " \n" if not i == longestWordLength - 1 else " "

        resultString += xLabel

    return resultString
