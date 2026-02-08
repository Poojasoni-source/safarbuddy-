class Payment:
  def __init__(self,amount):
    self.amount=amount
    self.status='pending'
  def pay(self):
        raise NotImplementedError#This method is meant to be overridden in child classes, not used directly.
#So we are forcing the programmer to implement pay() in subclasses.
class UPIPayment(Payment):
  def pay(self):
    self.status='completed'
    print("paid using UPI")
class CardPayment(Payment):
    def pay(self):
        self.status = "Completed"
        print("Paid using Card")
#polymorphism in above payment methods as pay method is used for different behaviour
