from stats import get_text_length, get_char_dict, sort_char_dict
import sys

def get_book_text(file_path):
    with open(file_path, encoding='utf-8-sig') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_text_length(text)
    char_freq = get_char_dict(text)
    sorted_chars = sort_char_dict(char_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

main()