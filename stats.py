
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def number_of_words():
    num_words = len(get_book_text("./books/frankenstein.txt").split() )
    print(num_words,"words found in the document")

num_words = {}

def number_of_signs():
    lower_signs = get_book_text("./books/frankenstein.txt").lower()
    #print(lower_signs)
    #num_words = {}
    for element in lower_signs:
        if element in num_words:
            sign = int(num_words[element])
            #print(sign)
            num_words[element] = (sign + 1)
        else:
            num_words[element] = 1
    return(num_words)

dictionaty_list = []

def dic_list():
    for item in num_words:
        new_dic = {}
        key = item
        value = int(num_words[item])

        new_dic[item] = value
        dictionaty_list.append(new_dic)
    print(dictionaty_list)





       
