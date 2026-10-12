from functools import wraps

def required_role(allowed_role="admin"):
    def decoratore_role(func):
        @wraps(func)
        def wrapper(*args, **kwargs):  
            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print(f"Permission Denied: User is not an {allowed_role}.")
                return None

        return wrapper
    return decoratore_role

# Example Usage:
@required_role(allowed_role="admin")
def delete_database(user_role):
    print("Database deleted successfully!")

print("Test 1: Admin ")
delete_database(user_role="admin")

print("\nTest 2: Guest ")
delete_database(user_role="guest")