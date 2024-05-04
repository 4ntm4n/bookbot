def main():
    book_path = "books/frankenstein.txt"
    book_text = read_text(book_path)
    num_of_words = word_count(book_text)
    num_of_letters = letter_count(book_text)
    print(f"{num_of_words} words found in the document")
    print(f"{num_of_letters}")

# made it count letters from the alphabet and not any char.
def letter_count(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {}
    for l in text:
        lower_l = l.lower()
        if lower_l in letters:
            if lower_l in letter_count:
                letter_count[lower_l] += 1
            else:
                letter_count[lower_l] = 1           
    return letter_count

def word_count(text):
    words_list = text.split()
    return len(words_list)

def read_text(path):
    with open(path) as f:
        return f.read()

main()