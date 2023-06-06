import qrcode
import os
from django.conf import settings

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    qr_path = os.path.join(settings.MEDIA_ROOT, 'qr')
    file_path = os.path.join(qr_path, file_name)
    image.save(file_path)
    return "/qr/" + file_name

