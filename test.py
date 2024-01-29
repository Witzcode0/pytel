import qrcode

# Your multiple pieces of information
info1 = "First piece of information"
info2 = "Second piece of information"
info3 = "Third piece of information"

# Create a dictionary to hold the information
data_dict = {
    "info1": info1,
    "info2": info2,
    "info3": info3
}

# Convert the dictionary to a JSON string
import json
data_to_encode = json.dumps(data_dict)

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data_to_encode)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

# Alternatively, you can show the image
img.show()
