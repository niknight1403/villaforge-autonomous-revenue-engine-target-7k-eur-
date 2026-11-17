import { test } from 'node:test';
import assert from 'node:assert';
import { execSync } from 'node:child_process';

test('Smoke Test: Engine Core Initialization', () => {
  const output = execSync('python3 -c "from src.engine import RevenueEngine; print(RevenueEngine().status())"').toString().trim();
  assert.strictEqual(output, 'READY');
});

test('Build Integrity: Check source files', () => {
  const files = execSync('ls src/').toString();
  assert.ok(files.includes('engine.py'));
});