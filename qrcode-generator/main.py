import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of the qrcode
    border=4,  # border between background and qrcode
)
qr.add_data('url')  # add url here
qr.make(fit=True)

# rgb color is allowed: back_color = (255, 255, 255)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.jpg')  # file format must be jpg or png
