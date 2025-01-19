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
def generateReport(bookname, word_count, char_dictionary):
    report = f"--- Begin report of {bookname} ---\n"
    report = report + f"{word_count} words found in the document\n\n"
    for char in char_dictionary:
        if char.isalpha():
            report = report + f"The \'{char}\' character was found {char_dictionary[char]} times\n"
    report = report + f"--- End Report ---"
    return report


def main():
    bookpath = "books/frankenstein.txt"
    with open(bookpath) as f:
        file_contents = f.read()
        word_count = WordCount(file_contents)
        char_dictionary = charCount(file_contents)
        #char_dictionary.sort(reverse=True)
        print(generateReport(bookpath, word_count, char_dictionary))

main()