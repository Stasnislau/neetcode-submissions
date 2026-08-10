class TimeMap {
    constructor() {
        this.keyStore = new Map();
        this.timeStore = new Map();
    }

    set(key, value, timestamp) {
        const fullKey = `${key}#${timestamp}`;
        // Тут все заебись, только давай сразу создадим массив если его нет
        if (!this.timeStore.has(key)) {
            this.timeStore.set(key, []);
        }
        this.timeStore.get(key).push(timestamp);
        this.keyStore.set(fullKey, value);
    }

    get(key, timestamp) {
        // Сначала проверяем прямое попадание
        const directHit = this.keyStore.get(`${key}#${timestamp}`);
        if (directHit) return directHit;

        const timestamps = this.timeStore.get(key);
        if (!timestamps || timestamps.length === 0) return "";

        // Важные проверки граничных случаев
        if (timestamp < timestamps[0]) return "";
        if (timestamp >= timestamps[timestamps.length - 1]) {
            return this.keyStore.get(`${key}#${timestamps[timestamps.length - 1]}`);
        }

        // Бинарный поиск
        let left = 0;
        let right = timestamps.length - 1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (timestamps[mid] === timestamp) {
                return this.keyStore.get(`${key}#${timestamps[mid]}`);
            }
            if (timestamps[mid] < timestamp) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // После бинарного поиска right указывает на ближайший меньший timestamp
        return this.keyStore.get(`${key}#${timestamps[right]}`);
    }
}