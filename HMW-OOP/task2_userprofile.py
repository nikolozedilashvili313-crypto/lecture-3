class User:
    status = "Active"
    
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"User - {self.username} with email {self.email} is {self.age} years old and has {User.status} status")

username1 = User("Nika", "nika@example.com", 25)
username2 = User("Giorgi", "giorgi@example.com", 30)

username1.get_info()
username2.get_info()
