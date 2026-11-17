const http = require('http');
const options = { hostname: 'localhost', port: 3000, path: '/health', method: 'GET' };
const req = http.request(options, (res) => {
  if (res.statusCode === 200) {
    console.log('Health check passed');
    process.exit(0);
  } else {
    console.error('Health check failed with status:', res.statusCode);
    process.exit(1);
  }
});
req.on('error', (e) => {
  console.error('Request error:', e.message);
  process.exit(1);
});
req.end();