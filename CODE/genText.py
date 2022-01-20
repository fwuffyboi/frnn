def oneStep2():
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.layers.experimental import preprocessing

    import time

    print("TensorFlow Version: ", str(tf.__version__))

    path_to_file = "I:\\PROGRAMMING\\currentProjects\\PROJECT-FRNN\\TrainingData.txt"
    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    vocab = sorted(set(text))

    ids_from_chars = preprocessing.StringLookup(
        vocabulary=list(vocab), mask_token=None)

    chars_from_ids = tf.keras.layers.experimental.preprocessing.StringLookup(
        vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None)

    # Define a simple sequential model
    def create_model():
        model = tf.keras.models.Sequential([
            keras.layers.Dense(512, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                      loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=[tf.metrics.SparseCategoricalAccuracy()])

        return model

    filepath = "I:\\PROGRAMMING\\currentProjects\\PROJECT-FRNN\\PROJECT_FRNN_MODEL"

    # Create a basic model instance
    model = create_model()

    # Display the model's architecture
    model = tf.keras.models.load_model(filepath)
    model.summary()



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
                values=[-float('inf')] * len(skip_ids),
                indices=skip_ids,
                # Match the shape to the vocabulary
                dense_shape=[len(ids_from_chars.get_vocabulary())])
            self.prediction_mask = tf.sparse.to_dense(sparse_mask)

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
            predicted_logits = predicted_logits / self.temperature
            # Apply the prediction mask: prevent "[UNK]" from being generated.
            predicted_logits = predicted_logits + self.prediction_mask

            # Sample the output logits to generate token IDs.
            predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
            predicted_ids = tf.squeeze(predicted_ids, axis=-1)

            # Convert from token ids to characters
            predicted_chars = self.chars_from_ids(predicted_ids)

            # Return the characters and model state.
            return predicted_chars, states

    one_step_model = OneStep(model, chars_from_ids, ids_from_chars)

    start = time.time()
    states = None
    next_char = tf.constant(['ROMEO:'])
    result = [next_char]

    for n in range(100):
        next_char, states = one_step_model.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)
    end = time.time()
    print(result[0].numpy().decode('utf-8'), '\n\n' + '_' * 80)
    print('\nRun time:', end - start)


oneStep2()
