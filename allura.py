import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.layers import Embedding, LSTM, Dense, CuDNNLSTM
from keras.models import load_model
import numpy as np

model = load_model("allura.h5")
text = open("Conversation.txt", encoding="utf-8").read()

# Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1  # Add 1 for the '0' padding token

# Create input sequences and labels
input_sequences = []
for line in text.split('\n'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# Pad sequences
max_sequence_length = max([len(seq) for seq in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

def predict_next_word(seed_text, next_words):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
        predicted_probabilities = model.predict(token_list, verbose=0)
        predicted_class = np.argmax(predicted_probabilities)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_class:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Test the next-word prediction
seed_text = ""
predicted_text = predict_next_word(seed_text, next_words=5)
print(predicted_text)