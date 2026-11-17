const http = require('http');
const assert = require('assert');

const options = { hostname: 'localhost', port: 3000, path: '/api/dashboard', method: 'GET' };

const req = http.request(options, (res) => {
  assert.strictEqual(res.statusCode, 200);
  console.log('Test Passed: Dashboard reachable');
  process.exit(0);
});

req.on('error', (e) => {
  console.error(`Test Failed: ${e.message}`);
  process.exit(1);
});

req.end();