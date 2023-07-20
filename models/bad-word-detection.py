import csv

def load_hate_words(file_path):
    hate_words = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for word in row:
                word = word.strip().lower()
                if word:
                    hate_words.add(word)
    return hate_words

def detect_hate_words(sentence, hate_words):
    preprocessed_sentence = sentence.lower().strip()
    tokens = preprocessed_sentence.split()

    for token in tokens:
        if token in hate_words:
            return True  # Hate word detected

    return False  # No hate word detected

# Load hate words from CSV file
hate_words = load_hate_words('bad-words.csv')

# Example usage
input_sentence = input("Enter a sentence: ")
if detect_hate_words(input_sentence, hate_words):
    print("Hate word detected!")
else:
    print("No hate word detected.")
