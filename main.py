def main():
    book_path = "books/frankenstein.txt"
    book_text = read_text(book_path)
    num_of_words = word_count(book_text)
    chars = char_count(book_text)
    char_analysis = get_char_analysis(chars)

  
    print(f"This book has {num_of_words} words... \n")
    print("Here comes a character analyis on this book:")
    for ch in char_analysis:
        print(f"character {ch["char"]} is found {ch["number"]} times")


def get_num(dict):
    return dict["number"]

def get_char_analysis(dict):
    stats = []
    for key in dict:
        stats.append({"char": key, "number": dict[key]})

    stats.sort(key=get_num, reverse=True)
    return stats
    

def char_count(text):
    filter = "abcdefghijklmnopqrstuvwxyz"
    char = {}
    for c in text:
        lc = c.lower()
        if lc in filter:
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
