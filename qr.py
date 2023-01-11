from flask import Flask, request, jsonify, Response
import qrcode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/qr-code', methods=['GET'])
def generate_qr_code():
    # Get the URL from the query string
    url = request.args.get('url')
    if not url:
        return jsonify(message='No URL provided'), 400

    # Create a QR code image
    img = qrcode.make(url)

    # Save the QR code image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)

    # Create the response
    response = Response(buffer.getvalue(), content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='qr-code.png')
    return response



if __name__ == '__main__':
    app.run()
