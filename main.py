
def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_the_words(file_contents)
    character_count = count_characters(file_contents)
    create_report(path_to_file, word_count, character_count)


def count_the_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}

    for t in text:
        if t.isalpha():
            lower_t = t.lower()
            if lower_t not in characters:
                characters[lower_t] = 1
            else:
                characters[lower_t] += 1
        
    return characters


def create_report(book, words, characters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")

    for k in characters.keys():
        print(f"The '{k}' character was found {characters[k]} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()