class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class User(Person):
  #properties
  def __init__(self,name,phone,address,identity,emergency_contact):
    super().__init__(name, phone)
    self.address=address
    self.identity=identity
    self.emergency_contact=emergency_contact
    self.active_trips = []
    self.completed_trips = []
  def to_dict(self):
      return {
          'user_name':self.name,
          'user_phone':self.phone,
          'user_address':self.address,
          'users_emergency_contact':self.emergency_contact,
          'users_identity':self.identity
      }
  @classmethod
  def from_dict(cls,data):
      return cls(data['user_name'],
                 data['user_phone'],
                 data['user_address'],
                 identity=None,
                 emergency_contact=None)
      
  def create_trip(self, trip):
      self.active_trips.append(trip)
      print(f"{self.name} created trip {trip.trip_id}")


  def join_trip(self, trip):
      trip.add_member(self)
      self.active_trips.append(trip)
      print(f'{self.name} joined trip{trip.trip_id}')


  def cancel_trip(self, trip):
      if trip in self.active_trips:
          self.active_trips.remove(trip)
          print(f"{self.name} cancelled trip {trip.trip_id}")
  def __repr__(self):
        # This controls how the object prints
        return f"User(name={self.name!r}, phone={self.phone!r}, address={self.address!r}, identity={self.identity!r}, emergency_contact={self.emergency_contact!r})"