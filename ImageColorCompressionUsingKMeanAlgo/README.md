README.md — Image Color Compression using K‑Means Clustering
🌟 Overview
This project demonstrates image color compression using K‑Means clustering.
The idea is simple:

An image contains thousands or millions of colors.

K‑Means groups similar colors into K clusters.

Each pixel is replaced with its cluster’s centroid color.

The result is a compressed, stylized image with fewer colors.

This technique is commonly used for:

Posterization

Artistic effects

Reducing image size

Preprocessing for computer vision tasks

🧠 How It Works
✔ 1. Load the image
The image is loaded using Pillow (PIL) and converted into a NumPy array.

✔ 2. Flatten the image
RGB images have shape:
(height, width, 3)

We reshape it into:

(num_pixels, 3)
so K‑Means can treat each pixel as a 3‑dimensional point (R, G, B).

✔ 3. Apply K‑Means
We cluster all pixels into K = 4 color groups.

✔ 4. Replace each pixel
Each pixel is replaced with the centroid color of its assigned cluster.

✔ 5. Reshape and save
The compressed pixel array is reshaped back to the original image shape and saved.