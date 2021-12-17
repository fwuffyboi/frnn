def oneStep2():
    import tensorflow as tf
    one_step_reloaded = tf.saved_model.load(
        "C:\\Users\\User1\\Desktop\\Desktop\\PROJECTS\\currentProjects\\PROJECT-FRNN\\PROJECT_FRNN_MODEL")

    states = None
    next_char = tf.constant(['ROMEO:'])
    result = [next_char]

    for n in range(100):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    print(tf.strings.join(result)[0].numpy().decode("utf-8"))


oneStep2()
