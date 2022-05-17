import matplotlib
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# https: // stackoverflow.com/questions/53684971/assertion-failed-flask-server-stops-after-script-is-run
matplotlib.use('Agg')


def get_category(img):
    # # Read an image from a file into a numpy array
    img = mpimg.imread(img)
    # # Convert to float32
    img = tf.cast(img, tf.float32)
    # # Resize to 224x224 (size the model is expecting)
    img = tf.image.resize(img, [550, 550])
    # # Expand img dimensions from (224, 224, 3) to (1, 224, 224, 3) for set_tensor method call
    # img = np.expand_dims(img, axis=0)
    # print('2')
    # tflite_model_file = 'static/model/model.tflite'
    # print('3')
    # with open(tflite_model_file, 'rb') as fid:
    #     tflite_model = fid.read()

    # print('model read')

    # interpreter = tf.lite.Interpreter(model_content=tflite_model)
    # interpreter.allocate_tensors()

    # print('interpreter')

    # input_index = interpreter.get_input_details()[0]["index"]
    # output_index = interpreter.get_output_details()[0]["index"]

    # prediction = []
    # interpreter.set_tensor(input_index, img)
    # interpreter.invoke()
    # prediction.append(interpreter.get_tensor(output_index))

    # predicted_label = np.argmax(prediction)
    # class_names = ['rock', 'paper']

    # return class_names[predicted_label]
