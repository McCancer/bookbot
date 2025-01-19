#returns the number of words in the given string
def WordCount(input_string):
    return len(input_string.split())

#Returns a dictionary key is the char and value is number of occurances 
#ex {'p' : 1000, 'q' : 2000}
def charCount(input_string):
    chars = {}
    for char in input_string:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

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
    report = report + f"--- End Report ---"
    return report

#used the the char_dict_to_sorted_list function to sort the dictionary
def sort_on(d):
    return d["num"]

#Given a dictionary of chars it will turn it to a sorted list
#ex [{"char" : 'p', "num" : 1000}, {"char" : 'q', "num" : 2000}]
def char_dict_to_sorted_list(char_dictionary):
    sorted_list = []
    for ch in char_dictionary:
        sorted_list.append({"char": ch, "num": char_dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#given a file path to a text file it will return that text file as a string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    #Set book file path / path to text file
    book_path = "books/frankenstein.txt"
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