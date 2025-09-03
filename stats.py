def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def count_characters(path):
    text = get_book_text(path)
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list