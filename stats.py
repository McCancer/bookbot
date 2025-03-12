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