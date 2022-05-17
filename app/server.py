import os
import tensorflow as tf
import numpy as np
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['IMAGE_UPLOADS'] = os.path.join(APP_ROOT, 'static')

# load the model file
model = tf.keras.models.load_model(os.path.join(APP_ROOT, 'InceptionV3_Siamese_Model.h5'))

def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (100, 100))
    img = img / 255.0
    return img

def cosine_similarity(anc, inp):
    return np.dot(anc[0], inp[0]) / (np.linalg.norm(anc[0]) * np.linalg.norm(inp[0]))

@app.route("/face-similarity", methods=["GET", "POST"])
def similarity_score():
    if request.method == "POST":
        image_one = request.files['image_one']
        image_two = request.files['image_two']

        path_one = os.path.join(app.config["IMAGE_UPLOADS"], image_one.filename)
        path_two = os.path.join(app.config["IMAGE_UPLOADS"], image_two.filename)

        image_one.save(path_one)
        image_two.save(path_two)

        anc_img = preprocess(path_one)
        inp_img = preprocess(path_two)

        anc_encoding, _, inp_encoding = model.predict(list(np.expand_dims([anc_img, inp_img, inp_img], axis=1)))

        distance = cosine_similarity(anc_encoding, inp_encoding)

        return jsonify(similarity=str(distance))

    return make_response("No Images Selected", 202)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)











