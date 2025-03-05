from stats import get_number_of_words
from stats import get_char_count

def main():
    num_words = get_number_of_words()
    print(f"{num_words} words found in the document")
    num_of_chars = get_char_count()
    print(num_of_chars)

main()