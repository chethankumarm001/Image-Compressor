import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
import io

def compress_image(image_file, k):
    """
    Compress a color image using PCA and return:
    - compressed image (as bytes)
    - compression stats
    """

    # Load image from uploaded file
    original_img = Image.open(image_file).convert("RGB")
    X_original = np.array(original_img)
    M, N, C = X_original.shape

    # Safety check
    if k >= min(M, N):
        k = min(M, N)

    original_data_size = M * N * C
    compressed_data_points_per_channel = (M * k) + (N * k) + N
    total_compressed_data_size = compressed_data_points_per_channel * C

    reconstructed_channels = []
    mse_list = []

    # Process R, G, B channels separately
    for i in range(C):
        channel = X_original[:, :, i]

        pca = PCA(n_components=k)
        X_compressed = pca.fit_transform(channel)
        X_reconstructed = pca.inverse_transform(X_compressed)

        mse = np.mean((channel - X_reconstructed) ** 2)
        mse_list.append(mse)

        reconstructed_channels.append(
            np.clip(X_reconstructed, 0, 255).astype(np.uint8)
        )

    # Combine channels back into color image
    X_reconstructed_color = np.stack(reconstructed_channels, axis=2)

    # Convert numpy → image → bytes (for Django)
    output_img = Image.fromarray(X_reconstructed_color)
    img_byte_arr = io.BytesIO()
    output_img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    stats = {
        "original_size": original_data_size,
        "compressed_size": total_compressed_data_size,
        "compression_ratio": round(original_data_size / total_compressed_data_size, 2),
        "mse": round(float(np.mean(mse_list)), 2),
    }

    return img_byte_arr, stats