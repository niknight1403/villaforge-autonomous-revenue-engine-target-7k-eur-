from src.engine import RevenueEngine

def main():
    engine = RevenueEngine()
    current_mrr = 0
    gap = engine.get_target_gap(current_mrr)
    print(f'Target: 7000 EUR MRR')
    print(f'Current: {current_mrr} EUR MRR')
    print(f'Gap: {gap} EUR MRR')

if __name__ == '__main__':
    main()