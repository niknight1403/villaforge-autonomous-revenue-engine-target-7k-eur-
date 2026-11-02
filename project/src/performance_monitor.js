/**
 * Performance Monitoring Module
 * Ensures load times < 1s for optimal conversion rates.
 */
(function() {
    window.addEventListener('load', () => {
        setTimeout(() => {
            const [navigation] = performance.getEntriesByType('navigation');
            const loadTime = navigation.loadEventEnd;
            console.log(`[Performance] Page Load Time: ${loadTime.toFixed(2)}ms`);
            
            if (loadTime > 1000) {
                console.warn('[Performance] Warning: Load time exceeds 1s threshold.');
            }
        }, 0);
    });
})();