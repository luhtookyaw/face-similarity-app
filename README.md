# Face Similarity Score Docker App

Cosine Similarity between two encodings of two faces which are mapped from Inception Siamese network.

### Pull image from docker hub repository
```python
docker pull barry4holly/face-similarity-app:0.1.1
```


### Run image with remove option
```
docker run --rm -p 8000:8000 barry4holly/face-similarity-app:0.1.1
```


### Inference with curl to service
```python
curl -i -X POST \
    -H "Content-Type: multipart/form-data" \
    -F "image_one=@anchor_00009.jpg" \
    -F "image_two=@anchor_00010.jpg" \
    http://localhost:8000/face-similarity
```