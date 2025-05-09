import qrcode
import os
import streamlit as st
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

# ---------------- QR Generator ---------------- #

def generate_qr(data, version=1, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_L):
    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        return img
    except Exception as e:
        st.error(f"An error occurred while generating QR: {e}")
        return None

# ---------------- QR Decoder ---------------- #

def decode_qr_with_opencv(uploaded_file):
    try:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        data, points, _ = detector.detectAndDecode(img)
        return data
    except Exception as e:
        st.error(f"An error occurred while decoding: {e}")
        return None

# ---------------- Streamlit UI ---------------- #

st.set_page_config(page_title="QR Code Generator & Decoder", layout="centered")
st.title("📌 QR Code Generator & Decoder")

tabs = st.tabs(["📤 Generate QR Code", "📥 Decode QR Code"])

# --------- QR Generator Tab --------- #
with tabs[0]:
    st.subheader("Generate QR Code")

    data = st.text_input("Enter the text or URL to encode:")
    filename = st.text_input("Filename to save (e.g., myqr.png):", value="qrcode.png")

    version = st.slider("QR version (1–40)", 1, 40, 1)
    box_size = st.number_input("Box size", min_value=1, value=10)
    border = st.number_input("Border size", min_value=1, value=4)

    error_correction_level = st.selectbox(
        "Error correction level",
        options=["L", "M", "Q", "H"],
        index=0,
        help="Higher levels tolerate more damage, but increase size."
    )

    error_correction_dict = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }
    error_correction = error_correction_dict[error_correction_level]

    if st.button("Generate"):
        if not data:
            st.error("Please enter data to encode.")
        else:
            img = generate_qr(data, version, box_size, border, error_correction)
            if img:
                st.success("✅ QR code generated!")

                # Convert image to bytes
                buf = BytesIO()
                img.save(buf, format="PNG")
                byte_img = buf.getvalue()

                st.image(byte_img, caption="Your QR Code", use_container_width=False)

                img_path = os.path.join("generated_qrs", filename)
                os.makedirs("generated_qrs", exist_ok=True)
                img.save(img_path)

                with open(img_path, "rb") as f:
                    st.download_button("📥 Download QR Code", f, file_name=filename, mime="image/png")

# --------- QR Decoder Tab --------- #
with tabs[1]:
    st.subheader("Decode QR Code")

    uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded QR Code", use_container_width=False)
        decoded_text = decode_qr_with_opencv(uploaded_file)

        if decoded_text:
            st.success("✅ QR Code Decoded:")
            st.code(decoded_text, language="text")
        else:
            st.warning("❌ No QR code detected or unreadable image.")
