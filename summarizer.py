import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data
nltk.download('punkt', quiet=True)  # for tokenizing sentences, quiet=True suppresses the confirmation message
nltk.download('stopwords', quiet=True)  # for removing stop words

def summarize_text(text, max_sentences=5):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Removing stop words and making a frequency table of words
    stop_words = set(stopwords.words("english"))
    freq_table = dict()
    for word in words:
        if word in stop_words or word.isalpha() == False:  # Also, check if the word is alphabetic to remove punctuation
            continue
        freq_table[word] = freq_table.get(word, 0) + 1  # More concise way to handle word frequency

    # Scoring sentences by summing up the frequencies of the words that appear in them
    sentence_value = dict()
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                sentence_value[sentence] = sentence_value.get(sentence, 0) + freq

    # Getting the average score for a sentence in the text
    average = sum(sentence_value.values()) / len(sentence_value) if sentence_value else 0

    # Generating the summary: sentences with a score above the average get included
    summary = ' '.join(sentence for sentence in sentences if sentence_value.get(sentence, 0) > (1.2 * average))

    return summary

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])  # This will allow the script to take multi-word arguments
        print(summarize_text(input_text))
    else:
        print("Please provide text to summarize as an argument.")
