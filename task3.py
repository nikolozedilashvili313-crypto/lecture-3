def greeter_bot():
    name = yield "Enter your name: "

    while True:
        name = yield f"Hello, {name}!"

bot = greeter_bot()
print(next(bot))

user_input = input("--")
print(bot.send(user_input)) 

while True:
    user_input = input("Enter another name (or enter q to quit): ")
    
    if user_input.lower() == "q":
        print("Exited the greeter bot.")
        break
    
print(bot.send(user_input))