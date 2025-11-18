import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create a QRCode object with custom settings
qr = qrcode.QRCode(
    version=1,  # QR code size (1 to 40, 1 is 21x21 matrix)
    error_correction=ERROR_CORRECT_H,  # Error correction level (L, M, Q, H)
    box_size=10,  # Number of pixels per "box" of the QR code
    border=4,  # Thickness of the border (in boxes)
)

# Add data to the QR code
qr.add_data("Some custom data or URL")
qr.make(fit=True)  # Automatically adjust the size to fit the data

# Create the image with custom colors
img = qr.make_image(fill_color="darkblue", back_color="lightblue")

# Save the image
img.save("custom_qrcode.png")