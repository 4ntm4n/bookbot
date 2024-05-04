def main():
    book_path = "books/frankenstein.txt"
    book_text = read_text(book_path)
    num_of_words = word_count(book_text)
    num_of_char = char_count(book_text)
    print(f"{num_of_words} words found in the document")
    print(f"{num_of_char}")

def char_count(text):
    char = {}
    for c in text:
        lc = c.lower()
        if lc in char:
            char[lc] += 1
        else:
            char[lc] = 1
    return char


def word_count(text):
    words_list = text.split()
    return len(words_list)


def read_text(path):
    with open(path) as f:
        return f.read()


main()
