def sort_second(dict):
    return dict[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = 0
    for word in book_contents.split():
        num_words += 1
    return num_words

def get_char_count():
    book_contents = (get_book_text("books/frankenstein.txt")).lower()
    char_dict = {}
    char_count = 1
    for char in book_contents:
        if char in char_dict:
            char_dict[char] += char_count
        else:
            char_dict[char] = char_count
    return char_dict 

def get_sorted_chars(dict):
    char_list = list(dict.items())
    char_list.sort(reverse=True, key=sort_second)
    return char_list