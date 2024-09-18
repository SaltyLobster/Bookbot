def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words_in_string(text)
    chars_dict = count_the_number_of_occurrences(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found '{item['num']}' times")
    print("--- End report ---")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words_in_string(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_the_number_of_occurrences(text):
    chars_dict = {}
    for char in text.lower():
        if char.isalpha() and char not in chars_dict:
            chars_dict[char] = 1
        elif char.isalpha():
            chars_dict[char] += 1
    return chars_dict


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()