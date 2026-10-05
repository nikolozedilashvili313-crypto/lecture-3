def create_user_profile(first_name, last_name, is_active, role="student"):
 return {
    "first_name": first_name,
    "last_name": last_name,
    "is_active": is_active,
    "role": role
 }

f_name = input("Enter your first name: ").capitalize() 
l_name = input("Enter your last name: ").capitalize() 

user_profile = create_user_profile(f_name, l_name, role ="student", is_active = True)
print(user_profile)