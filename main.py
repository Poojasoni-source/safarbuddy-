from users import User
from storage import load_users, save_users

users = load_users()

print("Loaded users:")
for u in users:
    print(u)


choice=input("want to add new user?(y/n):")
if choice=='y':
    name=input('enter name')
    phone=input('enter phone')
    address=input('enter address')
    
    new_user = User(name,phone,address,emergency_contact=None,identity=None)
    users.append(new_user)
    save_users(users)

print("User saved successfully")