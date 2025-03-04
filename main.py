def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def number_of_words():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = 0
    for word in book_contents.split():
        num_words +=1
    return num_words

def main():
    num_words = number_of_words()
    print(f"{num_words} words found in the document")

main()