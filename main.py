def char_count(text):
    text = text.lower()
    all_characters = {}

    for character in text:
        if character not in all_characters:
            all_characters[character] = 1
        else:
            all_characters[character] += 1
    return all_characters


def main(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        words = file_contents.split()
        char_dict = char_count(file_contents)
        keys = list(char_dict.keys())
        keys.sort()
        sorted_dict = {i: char_dict[i] for i in keys}

        print(f"--- Begin report of {file_path} ---")
        print(f"{len(words)} words found in the document")
        for character in sorted_dict:
            print(f"The character '{character}' was found {sorted_dict[character]} times")
        print("--- End report ---")


if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    main(file_path)
