const { exec } = require('child_process');
exec('python3 --version', (error, stdout, stderr) => {
  if (error) {
    console.error('python3 not found:', error);
  } else {
    console.log(stdout.trim());
  }
});