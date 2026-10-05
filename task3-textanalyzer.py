def analyze_text(text, min_length=3, ignore_stopwords=None):
    
    if ignore_stopwords is None:
        ignore_stopwords = []

    words = text.split()

    count = 0
    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1
    return count



sample_text = "python is a great programming language to learn"
print(analyze_text(sample_text)) 
print(analyze_text(sample_text, min_length=4, ignore_stopwords=["great", "learn"]))