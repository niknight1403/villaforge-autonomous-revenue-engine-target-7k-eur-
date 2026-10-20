import os

def run_smoke():
    assert os.path.exists('index.html'), 'index.html not found'
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    assert len(content) > 0, 'index.html is empty'
    print('Smoke Test Passed: index.html verified successfully.')

if __name__ == '__main__':
    run_smoke()
