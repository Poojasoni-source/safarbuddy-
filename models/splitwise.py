class Expense:
    def __init__(self, paid_by, amount, participants):
        self.paid_by = paid_by        # User who paid
        self.amount = amount
        self.participants = participants  # list of users
    