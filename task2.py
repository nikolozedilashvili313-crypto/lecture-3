scores = [45, 82, 67, 38, 90, 55, 72]

# 1. Filter passing scores (>= 50) using filter() and lambda
passing_scores = list(filter(lambda score: score >= 50, scores))

# 2. Add 5 bonus points to each passing score (max 100) using map() and lambda
updated_scores = list(map(lambda score: score + 5 if score + 5 <= 100 else 100, passing_scores))

print(updated_scores)