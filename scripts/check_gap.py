from src.engine import RevenueEngine

def main():
    engine = RevenueEngine()
    current_mrr = 0
    gap = engine.get_target_gap(current_mrr)
    print(f'Gap to 7k: {gap}')

if __name__ == '__main__':
    main()