def main():
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    print(text)

def read_text(path):
    with open(path) as f:
        return f.read()
    
main()