const { execSync } = require('child_process');

const MAX_TIMEOUT_MS = 30000;
const RETRY_DELAY_MS = 300000;

function runTask(command, retries = 3) {
  try {
    console.log(`Executing: ${command}`);
    execSync(command, { timeout: MAX_TIMEOUT_MS, stdio: 'inherit' });
    console.log('Task completed successfully.');
  } catch (error) {
    const errorMessage = error.message || '';
    if (errorMessage.includes('LLM_UNAVAILABLE') || errorMessage.includes('QUOTA_EXCEEDED')) {
      console.error('Transient error detected. Marking as BLOCKED for retry...');
      process.exit(100); // Signal for retry-logic
    }
    console.error(`Task failed: ${error.message}`);
    process.exit(1);
  }
}

runTask(process.argv.slice(2).join(' '));