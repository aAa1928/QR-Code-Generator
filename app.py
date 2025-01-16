from flask import Flask, render_template
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
    img.save('qrcode.png')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()