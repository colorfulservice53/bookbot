import sys
from stats import get_num_words, char_count, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    bookstring = get_book_text(book_path)

    print("----------- Word Count ----------")
    book_wordcount = get_num_words(bookstring)
    print(f"Found {book_wordcount} total words")

    print("--------- Character Count -------")
    sorted_characters = sort_dict(char_count(bookstring))
    for i in sorted_characters:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")

def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

main()