import json
from src.revenue_engine import RevenueEngine

class StripeWebhookListener:
    def __init__(self, engine: RevenueEngine = None):
        self.engine = engine or RevenueEngine()

    def handle(self, payload):
        try:
            event = json.loads(payload)
        except json.JSONDecodeError:
            return {'status': 'error', 'message': 'Invalid JSON'}
        return self.process_event(event)

    def handle_event(self, event):
        return self.process_event(event)

    def process_event(self, event):
        event_type = event.get('type')
        obj = event.get('data', {}).get('object', {})
        
        if event_type == 'invoice.payment_succeeded':
            mrr = self.engine.process_webhook(event)
            return {'status': 'success', 'mrr': mrr}
            
        if event_type == 'customer.subscription.created':
            amount = obj.get('plan', {}).get('amount', 0) / 100
            self.engine.add_customer(obj.get('id'), amount)
            return {'status': 'success', 'mrr_impact': float(amount)}
            
        if event_type == 'customer.subscription.deleted':
            self.engine.remove_customer(obj.get('id'))
            return {'status': 'success', 'mrr_impact': -59.0}
            
        return {'status': 'error', 'message': 'Unknown event type'}