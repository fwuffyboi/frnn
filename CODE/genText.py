from trainRNN import chars_from_ids


def genText():
    import tensorflow as tf
    from tensorflow.keras.layers.experimental import preprocessing
    import numpy as np
    import os
    import time


    # where to find the file
    path_to_file = "../TrainingData.txt"

    # decode the file.
    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

    # print whatever this thing is
    vocab = sorted(set(text))
    print(f'{len(vocab)} unique characters')

    # Length of the vocabulary in chars
    vocab_size = len(vocab)

    # The embedding dimension
    embedding_dim = 256

    # idek
    ids_from_chars = preprocessing.StringLookup(
        vocabulary=list(vocab), mask_token=None)

    # Number of RNN units
    rnn_units = 1024


    class MyModel(tf.keras.Model):
        def __init__(self, vocab_size, embedding_dim, rnn_units):
            super().__init__(self)
            self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
            self.gru = tf.keras.layers.GRU(rnn_units,
                                           return_sequences=True,
                                           return_state=True)
            self.dense = tf.keras.layers.Dense(vocab_size)

        def call(self, inputs, states=None, return_state=False, training=False):
            x = inputs
            x = self.embedding(x, training=training)
            if states is None:
                states = self.gru.get_initial_state(x)
            x, states = self.gru(x, initial_state=states, training=training)
            x = self.dense(x, training=training)

            if return_state:
                return x, states
            else:
                return x


    model = MyModel(
        # Be sure the vocabulary size matches the `StringLookup` layers.
        vocab_size=len(ids_from_chars.get_vocabulary()),
        embedding_dim=embedding_dim,
        rnn_units=rnn_units)


    # below, this code makes a single step prediction.
    class OneStep(tf.keras.Model):
      def __init__(self, model, chars_from_ids, ids_from_chars, temperature=1.0):
        super().__init__()
        self.temperature = temperature
        self.model = model
        self.chars_from_ids = chars_from_ids
        self.ids_from_chars = ids_from_chars

        # Create a mask to prevent "[UNK]" from being generated.
        skip_ids = self.ids_from_chars(['[UNK]'])[:, None]
        sparse_mask = tf.SparseTensor(
            # Put a -inf at each bad index.
            values=[-float('inf')]*len(skip_ids),
            indices=skip_ids,
            # Match the shape to the vocabulary
            dense_shape=[len(ids_from_chars.get_vocabulary())])
        self.prediction_mask = tf.sparse.to_dense(sparse_mask)
        return chars_from_ids

      @tf.function
      def generate_one_step(self, inputs, states=None):
        # Convert strings to token IDs.
        input_chars = tf.strings.unicode_split(inputs, 'UTF-8')
        input_ids = self.ids_from_chars(input_chars).to_tensor()

        # Run the model.
        # predicted_logits.shape is [batch, char, next_char_logits]
        predicted_logits, states = self.model(inputs=input_ids, states=states,
                                              return_state=True)
        # Only use the last prediction.
        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits/self.temperature
        # Apply the prediction mask: prevent "[UNK]" from being generated.
        predicted_logits = predicted_logits + self.prediction_mask

        # Sample the output logits to generate token IDs.
        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)

        # Convert from token ids to characters
        predicted_chars = self.chars_from_ids(predicted_ids)
        print(predicted_chars)

        # Return the characters and model state.
        return predicted_chars, states


    # use model i think???
    one_step_model = OneStep(model, chars_from_ids, ids_from_chars)

    start = time.time()
    states = None
    next_char = tf.constant(['ROMEO:'])
    result = [next_char]

    print("line 121")

    for n in range(1000):
      next_char, states = one_step_model.generate_one_step(next_char, states=states)
      result.append(next_char)

    result = tf.strings.join(result)
    end = time.time()
    print(result[0].numpy().decode('utf-8'), '\n\n' + '_'*80)
    print('\nRun time:', end - start)

genText()
