import sys
from stats import *

#Generates a nice looking string report about book with given data
def generateReportFrmDictionary(bookname, word_count, char_dictionary):
    report = f"--- Begin report of {bookname} ---\n"
    report = report + f"{word_count} words found in the document\n\n"
    for char in char_dictionary:
        if char.isalpha():
            report = report + f"The \'{char}\' character was found {char_dictionary[char]} times\n"
    report = report + f"--- End Report ---"
    return report

#Generates a nice looking string report about book with given data
def generateReportFrmSortedList(bookname, word_count, char_list):
    report = f"--- Begin report of {bookname} ---\n"
    report = report + f"{word_count} words found in the document\n\n"
    for char in char_list:
        if char["char"].isalpha():
            report = report + f"The \'{char['char']}\' character was found {char['num']} times\n"
            #report = report + f"{char['char']}: {char['num']}\n"
    report = report + f"--- End Report ---"
    return report

#given a file path to a text file it will return that text file as a string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #get the text from the text file
    book_text = get_book_text(book_path)
    #get the word count of the file
    word_count = WordCount(book_text)
    #Get a dictionary of chars ex {'p' : 1000, 'q' : 2000}
    char_dictionary = charCount(book_text)
    #Turn Dictionary to a list of dictionaries that are sorted  #ex [{"char" : 'p', "num" : 1000}, {"char" : 'q', "num" : 2000}]
    sorted_char_list = char_dict_to_sorted_list(char_dictionary)
    #Generate and print the book/txt report
    print(generateReportFrmSortedList(book_path, word_count, sorted_char_list))

main()