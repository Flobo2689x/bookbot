import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = count_words(book_path)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(book_path)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
