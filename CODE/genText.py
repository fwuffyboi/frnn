def oneStep2():
    import tensorflow as tf
    print(tf.__version__)


    tf.saved_model.LoadOptions(
        allow_partial_checkpoint=False, experimental_io_device=None,
        experimental_skip_checkpoint=False
    )

    filepath = "C:\\Users\\User1\\Desktop\\Desktop\\PROJECTS\\currentProjects\\PROJECT-FRNN\\PROJECT_FRNN_MODEL"

    one_step_reloaded = tf.keras.models.load_model(
        filepath
    )
    # tf.saved_model.load(export_dir=filepath,)

    print(one_step_reloaded)

    states = None
    next_char = tf.constant(['ROMEO:'])
    result = [next_char]

    for n in range(100):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    print(tf.strings.join(result)[0].numpy().decode("utf-8"))


oneStep2()
