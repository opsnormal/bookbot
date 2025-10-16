# main code for bookbot - analysis of text of a book

from stats import get_book_text, get_characters, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    text = get_book_text(sys.argv[1])
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"Found {num_words} total words")

    char_dict = get_characters(text)

    sorted_chars = sort_dict(char_dict)

    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
            

main()