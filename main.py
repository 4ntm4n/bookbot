def main():
    book_path = "books/frankenstein.txt"
    book_text = read_text(book_path)
    num_of_words = word_count(book_text)
    print(f"{num_of_words} words found in the document")

def word_count(text):
    words_list = text.split()
    return len(words_list)

def read_text(path):
    with open(path) as f:
        return f.read()

main()