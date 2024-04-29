import json
import numpy as np
import pickle
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


responses = []
training_sentences = []
training_tags = []
unique_tags = []


# Result is a Python dictionary.
with open(r'C:\Users\tanvi\Desktop\intern\NLPChatbot\intents.json') as file:
    data = json.load(file)

# Iterating through the intents.json data
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_tags.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in unique_tags:
        unique_tags.append(intent['tag'])

# Calculate the number of unique tags/labels.
unique_tags_len = len(unique_tags)
le = LabelEncoder()
# Fit label encoder and return encoded tags/labels.
le.fit(training_tags)
# Transform tags/labels to normalized encoding.
training_tags = le.transform(training_tags)

vocab_size = 10000
oov_token = '<OOV>'
trunc_type = 'post'
embedding_dim = 16
max_len = 20

# Applying the Keras Preprocessing module to the defined lists
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, truncating=trunc_type, maxlen=max_len)

# Create Keras model.
model = tf.keras.models.Sequential()
model.add(keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(unique_tags_len, activation='softmax'))

#Model summary.
model.summary()


training_tags_ndarray = np.array(training_tags)
# Set Keras epoch value.
EPOCHS = 100

# Train model.
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(padded, training_tags_ndarray, epochs=EPOCHS)

# Save objects.
pickle_file = open('pickle_data.pickle', 'wb')
pickle.dump(data, pickle_file)
pickle.dump(le, pickle_file)
pickle.dump(tokenizer, pickle_file)
pickle_file.close()
# Save model.
tf.keras.models.save_model(model, "chatbot_model.h5")