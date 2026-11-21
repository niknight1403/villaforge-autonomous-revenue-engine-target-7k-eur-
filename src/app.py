from flask import Flask, request, jsonify
from engine import RevenueEngine

app = Flask(__name__)
engine = RevenueEngine()

@app.route('/mrr', methods=['POST'])
def get_mrr():
    data = request.json
    if not data or 'subscriptions' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    current_mrr = engine.calculate_mrr(data['subscriptions'])
    gap = engine.get_target_gap(current_mrr)
    
    return jsonify({
        'current_mrr': current_mrr,
        'target_gap': gap,
        'status': 'on_track' if gap == 0 else 'needs_growth'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)