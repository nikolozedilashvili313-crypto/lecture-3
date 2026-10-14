words = ["python", "generator", "yield", "code", "ai", "developer"]

word_generator = (word.upper() for word in words if len(word) > 4)

for word in word_generator:
    print(word)