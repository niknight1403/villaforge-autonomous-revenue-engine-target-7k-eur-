from flask import jsonify
from engine import RevenueEngine

engine = RevenueEngine()

def get_revenue_stats():
    try:
        stats = engine.calculate_current_mrr()
        return jsonify({
            'mrr': stats,
            'target': 7000,
            'gap': 7000 - stats,
            'status': 'active'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500