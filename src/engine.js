class RevenueEngine {
    constructor() {
        this.status = true;
    }

    checkStatus() {
        return this.status;
    }
}

const engine = new RevenueEngine();
if (engine.checkStatus()) {
    console.log('Engine ready');
    process.exit(0);
} else {
    process.exit(1);
}