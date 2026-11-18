from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import stripe
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/create-checkout-session', methods=['POST'])
@limiter.limit("5 per minute")
def create_checkout_session():
    try:
        data = request.json
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': data.get('price_id'),
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://your-app.com/success',
            cancel_url='https://your-app.com/cancel',
        )
        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)