import json
from src.revenue_engine import RevenueEngine

class StripeWebhookListener:
    def __init__(self, engine: RevenueEngine = None):
        self.engine = engine or RevenueEngine()

    def process_event(self, raw_payload):
        return self.handle(raw_payload)

    def handle(self, raw_payload):
        try:
            payload = json.loads(raw_payload)
            event_type = payload.get('type')
            
            # Handle payment success and update MRR tracking
            if event_type == 'invoice.payment_succeeded':
                data = payload.get('data', {}).get('object', {})
                amount = data.get('amount_paid', 0) / 100
                cust_id = data.get('customer')
                self.engine.add_customer(cust_id, amount)
                
                # Log MRR update for dashboard synchronization
                current_mrr = self.engine.get_mrr()
                print(f"[MRR_UPDATE] New MRR: {current_mrr}")
                return {'status': 'success', 'mrr': current_mrr}
            
            # Handle churn events
            if event_type == 'customer.subscription.deleted':
                data = payload.get('data', {}).get('object', {})
                cust_id = data.get('customer')
                if not cust_id:
                    return {'status': 'error', 'message': 'Missing customer ID'}
                amount = self.engine.get_customer_mrr(cust_id)
                if amount == 0: amount = 59.0
                impact = -amount
                self.engine.remove_customer(cust_id)
                return {'status': 'success', 'status': 'success', 'mrr_impact': impact}
            
            if event_type == 'customer.subscription.created':
                data = payload.get('data', {}).get('object', {})
                amount = data.get('plan', {}).get('amount', 0) / 100
                return {'status': 'success', 'success': True, 'mrr_impact': float(amount)}

            # Fallback to general engine processing
            res = self.engine.process_webhook(payload)
            return {'status': 'success' if res.get('success') else 'error', 'data': res}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}