from stats import get_num_words

from stats import get_num_characters

from stats import sort_characters

import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: Could not find the file {book_path}\nTry checking your file-path and try again")
        sys.exit(1)
    else:
        num_words = get_num_words(text)
        print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
        print(f"----------- Word Count ----------\nFound {num_words} total words")
        num_characters = get_num_characters(text)
        character_report = sort_characters(num_characters)
        print("--------- Character Count -------")
        for i in character_report:
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")

main()