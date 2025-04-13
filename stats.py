
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def number_of_words():
    num_words = len(get_book_text("./books/frankenstein.txt").split() )
    print("Found", num_words,"total words")

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

# def dic_list():
#     for item in num_words:
#         new_dic = {}
#         key = item
#         value = int(num_words[item])

#         new_dic[item] = value
#         dictionaty_list.append(new_dic)
#     print(dictionaty_list)

def dic_list_1():
    for item in num_words:
        new_dic = {}
        new_dic["letter"] = item
        new_dic["value"] = int(num_words[item])
        dictionaty_list.append(new_dic)
    return(dictionaty_list)

def sort_on(dictioary_list):
    return dictioary_list["value"]

def dic_sort():
    dictionaty_list.sort(reverse=True, key=sort_on)
    return(dictionaty_list)




       
