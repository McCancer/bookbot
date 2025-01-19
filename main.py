def WordCount(input_string):
    return len(input_string.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(numcount(file_contents))

main()