import tensorflow as tf


def full_summary(layer):
    if hasattr(layer, 'layers'):
        print('summary for ' + layer.name)
        layer.summary()
        print('\n\n')

        for l in layer.layers:
            full_summary(l)


model = tf.keras.models.load_model("out_test\\model-10.hdf5")
full_summary(model)
