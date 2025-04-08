
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def number_of_words():
    num_words = len(get_book_text("./books/frankenstein.txt").split() )
    print(num_words,"words found in the document")


def number_of_signs():
    lower_signs = get_book_text("./books/frankenstein.txt").lower()
    #print(lower_signs)
    num_words = {}
    for element in lower_signs:
        if element in num_words:
            sign = int(num_words[element])
            #print(sign)
            num_words[element] = (sign + 1)
        else:
            num_words[element] = 1
    print(num_words)