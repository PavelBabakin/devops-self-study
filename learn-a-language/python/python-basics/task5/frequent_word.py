def find_most_frequent_word(filename):
    with open(filename, 'r') as file:
        # Read the file and split it into words
        words = file.read().split()

        # Create a dictionary to store word frequency
        word_frequency = {}

        for word in words:
            # Convert word to lowercase and remove punctuation
            word = word.lower().strip('.,!?()[]{}":;')
            word_frequency[word] = word_frequency.get(word, 0) + 1

        # Find the most frequent word and its frequency
        most_frequent_word = max(word_frequency, key=word_frequency.get)
        frequency = word_frequency[most_frequent_word]

        return most_frequent_word, frequency

def main():
    filename = "sample_text.txt"
    word, frequency = find_most_frequent_word(filename)
    print(f"The most frequent word is '{word}' with a frequency of {frequency} times.")

if __name__ == "__main__":
    main()
