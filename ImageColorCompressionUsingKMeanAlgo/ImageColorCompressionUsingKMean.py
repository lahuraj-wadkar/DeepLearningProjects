from PIL import Image
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

img = Image.open("temple.jpg")
#img = img.convert("L")
#pixels = img.re

pixels = np.array(img)

pixels_2d = pixels.reshape(-1,3)

print(pixels.shape)

print(pixels_2d.shape)

model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10)
model = model.fit(pixels_2d)

print("Model Labels :", model.labels_.shape)
print(model.labels_)
compressed_pixels = model.cluster_centers_[model.labels_]

print(compressed_pixels.shape)
compressed_pixels_3d = compressed_pixels.reshape(pixels.shape).astype(np.uint8)
print(compressed_pixels_3d.shape)

compressed_img = Image.fromarray(compressed_pixels_3d)

compressed_img.save("Compresses_temple.jpg")