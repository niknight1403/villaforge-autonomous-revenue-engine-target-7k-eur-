import json

class RevenueEngine:
    def __init__(self, target_mrr):
        self.target_mrr = target_mrr
        self.customers = {}

    def add_customer(self, name, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        cust_id = name.lower().replace(' ', '_')
        cust = {'id': cust_id, 'name': name, 'amount': amount, 'active': True}
        self.customers[cust_id] = cust
        return cust

    def remove_customer(self, cust_id):
        if cust_id in self.customers:
            del self.customers[cust_id]
            return True
        return False

    def get_mrr(self):
        return sum(c['amount'] for c in self.customers.values())

    def update_mrr(self, amount):
        # Helper for testing/manual adjustments
        pass

    def get_current_mrr(self):
        return self.get_mrr()

    def forecast_revenue(self, months):
        if months < 0:
            raise ValueError('Months cannot be negative')
        return self.get_mrr() * months

    def process_webhook(self, payload):
        """Handles Stripe webhook events for subscription lifecycle management."""
        event_type = payload.get('type')
        data = payload.get('data', {}).get('object', {})
        
        if event_type == 'customer.subscription.created':
            cust_id = data.get('customer', 'unknown_user')
            amount = data.get('plan', {}).get('amount', 5900) / 100
            self.add_customer(cust_id, amount)
            return True
            
        if event_type == 'customer.subscription.deleted':
            cust_id = data.get('customer', 'unknown_user')
            return self.remove_customer(cust_id)
            
        if event_type == 'invoice.payment_succeeded':
            # Logic for tracking successful recurring payments
            return True

        if event_type == 'ping':
            return True
            
        return False