from flask import request, jsonify
import stripe
import os

def handle_stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError:
        return 'Invalid signature', 400

    if event['type'] == 'customer.subscription.created':
        subscription = event['data']['object']
        # Logic to update MRR in RevenueEngine goes here
    
    return jsonify({'status': 'success'}), 200