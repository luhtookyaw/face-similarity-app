# Face Similarity Score Docker App

Cosine Similarity between two encodings of two faces which are mapped from Inception Siamese network.

``curl -i -X POST \                                                     ✔
    -H "Content-Type: multipart/form-data" \
    -F "image_one=@anchor_00009.jpg" \
    -F "image_two=@anchor_00010.jpg" \
    http://localhost:8000/face-similarity
``