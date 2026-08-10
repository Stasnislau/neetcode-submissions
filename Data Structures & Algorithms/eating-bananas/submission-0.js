class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1;
        let r = Math.max(...piles);
        let min = Infinity;
        while (l <= r) {
            const middle = Math.floor((l + r) / 2);
            const currentH = piles.reduce((com, item) => {
                return com + Math.ceil(item / middle)
            }, 0)
            console.log(currentH, middle)
            if (currentH <= h) {
                if (middle < min) {
                    min = middle;
                }
                r = middle - 1;
            } else {
                l = middle + 1
            }
        }
        return min;
    }
}
