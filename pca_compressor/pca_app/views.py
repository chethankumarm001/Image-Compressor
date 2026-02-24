from django.shortcuts import render
from .forms import ImageUploadForm
from .utils.pca_compress import compress_image
import base64
from PIL import Image
import io

def compress_view(request):
    original_image_base64 = None
    compressed_image_base64 = None
    stats = None

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data["image"]
            k = form.cleaned_data["components"]   # ✔ back to original

            # Convert original image to Base64 for display
            original_img = Image.open(image).convert("RGB")
            buffer = io.BytesIO()
            original_img.save(buffer, format="PNG")
            original_image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

            # Reset file pointer before reusing the image
            image.seek(0)

            # Run PCA Compression
            compressed_bytes, stats = compress_image(image, k)

            # Convert compressed bytes to Base64
            compressed_image_base64 = base64.b64encode(compressed_bytes).decode("utf-8")

    else:
        form = ImageUploadForm()

    return render(request, "index.html", {
        "form": form,
        "original_image": original_image_base64,
        "compressed_image": compressed_image_base64,
        "stats": stats
    })