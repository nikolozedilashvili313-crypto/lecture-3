def favorite_writer_quote():
    writer_name = input("Enter the writer's name: ")
    quote = input("Enter the quote: ")

    with open("quotes.txt", "a", encoding = "utf-8") as file:
        file.write(f"{writer_name}: {quote}\n")
    print("Information saved successfully!")

def read_quotes():
    try:
        with open("quotes.txt", "r", encoding = "utf-8") as file:
            content = file.read()
            print("\n - Saved Quotes -")
            print(content)
    except FileNotFoundError:
        print("The file 'quotes.txt' does not exist. Please add a quote first.")

favorite_writer_quote()
read_quotes()