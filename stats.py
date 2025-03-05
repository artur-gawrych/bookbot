def sort_second(dict):
    return dict[1]

def get_number_of_words(book):
    num_words = 0
    for word in book.split():
        num_words += 1
    return num_words

def get_char_count(book):
    book_lower = book.lower()
    char_dict = {}
    char_count = 1
    for char in book_lower:
        if char in char_dict:
            char_dict[char] += char_count
        else:
            char_dict[char] = char_count
    return char_dict 

def get_sorted_chars(dict):
    char_list = list(dict.items())
    char_list.sort(reverse=True, key=sort_second)
    return char_list