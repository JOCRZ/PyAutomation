from PIL import Image
from io import BytesIO
import os

def process_image(input_path, output_path, width=None, height=None, quality=90, target_kb=None):
    """
    input_path   -> original image file path (any extension)
    output_path  -> output file path (any extension)
    width,height -> resize exactly to these values if BOTH given
                    maintain aspect ratio if only one is given
    quality      -> compression quality (1–100)
    target_kb    -> final output size in KB
    """

    # Load image
    img = Image.open(input_path)

    # ---------------- Resize Logic ----------------
    if width or height:
        w, h = img.size
        
        # If BOTH provided → force exact resize
        if width and height:
            img = img.resize((width, height), Image.LANCZOS)

        # Only width provided → scale height
        elif width and not height:
            height = int(h * (width / w))
            img = img.resize((width, height), Image.LANCZOS)

        # Only height provided → scale width
        elif height and not width:
            width = int(w * (height / h))
            img = img.resize((width, height), Image.LANCZOS)

    # ---------------- Output Format ----------------
    ext = os.path.splitext(output_path)[1].lower()
    save_format = ext.replace(".", "").upper()

    if save_format == "JPG":
        save_format = "JPEG"

    # JPEG cannot handle transparency
    if save_format == "JPEG" and img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # ---------------- No target size ----------------
    if target_kb is None:
        img.save(output_path, format=save_format, quality=quality)
        print("Saved:", output_path)
        return

    # ---------------- Compress to Target KB ----------------
    target_bytes = target_kb * 1024
    q = quality
    min_quality = 5
    step = 5

    while q >= min_quality:
        buffer = BytesIO()
        img.save(buffer, format=save_format, quality=q)
        size = buffer.tell()

        if size <= target_bytes:
            with open(output_path, "wb") as f:
                f.write(buffer.getvalue())
            print(f"Saved {output_path} at {size/1024:.2f} KB (quality={q})")
            return

        q -= step

    print("⚠ Cannot reach target size. Quality too low.")
    

# -------------------- EXAMPLE --------------------

# Here width AND height both are used (forced exact size)
process_image(
    input_path="input.png",
    output_path="output.jpg",
    width=200,
    height=300,     # both width + height → exact resize
    quality=90,
    target_kb=200
)
