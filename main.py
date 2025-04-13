from stats import number_of_words, number_of_signs, dic_list_1, sort_on, dic_sort
# def get_book_text(path_to_file):
#     with open(path_to_file) as f:
#         file_contents = f.read()
#     return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

# def number_of_words():
#     num_words = len(get_book_text("./books/frankenstein.txt").split() )
#     print(num_words,"words found in the document")

#main()
#number_of_words()
number_of_signs()
dic_list_1()

sorted_list = dic_sort()

print("============ BOOKBOT ============ \n\
Analyzing book found at books/frankenstein.txt...\n\
----------- Word Count ----------");
number_of_words()
print("--------- Character Count -------")
for i in sorted_list:
    if i["letter"].isalpha():
        l = i["letter"]
        v = i["value"]
        print(l,":", v,"\n")

print("============= END ===============")