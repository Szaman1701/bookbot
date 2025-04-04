def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

def number_of_words():
    num_words = len(get_book_text("./books/frankenstein.txt").split())
    print(num_words,"words found in the document")

#main()
number_of_words()

