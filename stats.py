def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        if not char.isalpha():
            continue
        normalized_char = char.lower()
        if normalized_char in char_count:
            char_count[normalized_char] += 1
        else:
            char_count[normalized_char] = 1
    return char_count

def get_sorted_char_counts(char_counts):
    sorted_char_counts = []
    for char, count in char_counts.items():
        sorted_char_counts.append({
            "char": char,
            "num": count
        })
    sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts

def sort_on(dict):
    return dict["num"]