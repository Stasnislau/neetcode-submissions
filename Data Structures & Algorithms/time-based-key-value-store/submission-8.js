class TimeMap {
    constructor() {
        this.keyStore = new Map();
        this.timeStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        const fullKey = key + "#" + timestamp;
        this.timeStore.set(key, [...(this.timeStore.get(key) || []), timestamp])
        this.keyStore.set(fullKey, value);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        const val = this.keyStore.get(key + '#' + timestamp)
        if (val)
            return val;
        const timestamps = this.timeStore.get(key) || [];
        if (!timestamps.length) return '';
        let l = 0;
        let r = timestamps.length - 1;
        if (timestamp < timestamps[l] )
            return ''
        if (timestamp >= timestamps[r]) {
            return this.keyStore.get(key + '#' + timestamps[r])
        }
        console.log(timestamps)
        while (l <= r) {
            let m = Math.floor((l + r) / 2);
            if (timestamps[m] > timestamp) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return this.keyStore.get(key + '#' + timestamps[r])

    }
}
