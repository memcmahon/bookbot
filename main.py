from stats import get_word_count, get_char_count, get_sorted_char_counts
import sys

def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_count(text)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for record in sorted_char_counts:
        print(f"{record['char']}: {record['num']}")
    print("============= END ===============")

main()