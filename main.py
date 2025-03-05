from stats import get_number_of_words
from stats import get_char_count
from stats import get_sorted_chars

def main():
    num_words = get_number_of_words()
    sorted_chars = get_sorted_chars(get_char_count())
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

main()