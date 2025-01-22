from time import time

from flask import Flask, render_template, request
from qrcode.main import QRCode
from qrcode.constants import ERROR_CORRECT_L

def generate_qrcode(data: str, *, box_size: int = 10, fill_color: str | tuple = 'black', back_color: str | tuple = 'white'):
    border_size: int = 2
    version: int = 1

    qr = QRCode(version=version,
                error_correction=ERROR_CORRECT_L,
                box_size=box_size,
                border=border_size)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save('static/images/qrcode.png')

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    timestamp = int(time())
    qr_generated = False

    if request.method == 'POST':
        url = request.form.get('url')
        fill_color = request.form.get('fillColor')
        back_color = request.form.get('bgColor')
        box_size = int(request.form.get('boxSize', 10))
        
        generate_qrcode(url, box_size=box_size, 
                       fill_color=fill_color, 
                       back_color=back_color)
        qr_generated = True

    return render_template('index.html', timestamp=timestamp, qr_generated=qr_generated)

if __name__ == '__main__':
    app.run()