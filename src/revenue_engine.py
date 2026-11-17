import json

class RevenueEngine:
    def __init__(self, target_mrr=7000):
        self.target_mrr = target_mrr
        self.customers = {}

    def add_customer(self, name, amount):
        if amount < 0:
            amount = 0
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
            cust_id = data.get('customer', 'unknown_user')
            amount = data.get('amount_paid', 0) / 100
            if cust_id in self.customers:
                self.customers[cust_id]['amount'] = amount
            else:
                self.add_customer(cust_id, amount)