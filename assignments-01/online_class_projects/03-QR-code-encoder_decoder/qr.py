import qrcode
import cv2

# Function to generate a QR Code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# Function to decode a QR Code
def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print(f"✅ Decoded Data: {data}")
    else:
        print("❌ No QR code found.")

# Main Code Execution
if __name__ == "__main__":
    # Step 1: Generate QR Code
    text = input("Enter text or URL to generate QR Code: ")
    generate_qr(text, "my_qrcode.png")

    # Step 2: Decode QR Code
    decode_qr("my_qrcode.png")