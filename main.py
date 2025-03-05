from stats import (
get_number_of_words,
get_char_count,
get_sorted_chars
)
from sys import argv

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    bookpath = argv[1]
    text = get_book_text(bookpath)
    num_words = get_number_of_words(text)
    sorted_chars = get_sorted_chars(get_char_count(text))
    print_report(bookpath, num_words, sorted_chars)

main()