from flask import Flask, request, jsonify
from flask_cors import CORS
import qrcode
import os
import base64
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Allows frontend to make requests from different origin

# Create QR-Generated folder if it doesn't exist
os.makedirs("QR-Generated", exist_ok=True)

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    """
    Endpoint to generate QR code
    Expects JSON: {"url": "https://example.com"}
    """
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        # Create QR code
        qr_obj = qrcode.QRCode()
        qr_obj.add_data(url)
        img = qr_obj.make_image()
        
        # Save to file
        filepath = "QR-Generated/qrcode.png"
        img.save(filepath)
        
        # Convert to base64 for display
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
        
        return jsonify({
            'message': 'QR generated successfully',
            'image': f'data:image/png;base64,{img_base64}',
            'filepath': filepath
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)