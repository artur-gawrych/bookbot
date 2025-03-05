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