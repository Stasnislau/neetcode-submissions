class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const stack = [];
        const cars = position.map((item, index) => [item, speed[index]]).sort((a, b) =>
            b[0] - a[0]
        )
        for (let i = 0; i < cars.length; i++) {
            const time = (target - cars[i][0]) / cars[i][1];
            stack.push(time);
            if (stack.length > 1) {
                if (stack[stack.length - 1] <= stack[stack.length - 2]) {
                    stack.pop();
                }
            }
        }
        return stack.length
    }
}
