class Trip:
    def __init__(self, trip_id, source, destination, host_user):
        self.trip_id = trip_id
        self.source = source
        self.destination = destination
        self.host_user = host_user
        self.members = [host_user]
        self.expenses = []
        self.status = "Planned"

    def add_member(self, user):
        self.members.append(user)

    def add_expense(self, amount):
        self.expenses.append(amount)

    def calculate_total_expense(self):
        return sum(self.expenses)

    def update_status(self, status):
        self.status = status
    def __repr__(self):
        return f'Trip(trip_id={self.trip_id!r},source={self.source!r} -> destination={self.destination!r},host_user={self.host_user!r})'