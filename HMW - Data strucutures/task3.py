phonebook = {
    "გიორგი": "+995 555 11 22 33",
    "ანა": "+995 555 22 33 44",
    "ნიკა": "+995 555 33 44 55",
    "მარიამი": "+995 555 44 55 66"
    }

search_name = "გიორგი"  

result = phonebook.get(search_name, "ვერ მოიძებნა")
print(f"ძიების შედეგი სახელზე '{search_name}': {result}")

search_name_2 = "დავითი"

result_2 = phonebook.get(search_name_2, "ვერ მოიძებნა")
print(f"ძიების შედეგი სახელზე '{search_name_2}': {result_2}")