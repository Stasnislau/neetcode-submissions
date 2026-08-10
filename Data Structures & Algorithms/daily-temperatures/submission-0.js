class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const stack = [];
        const res = new Array(temperatures.length).fill(0);
        for (let i = 0; i < temperatures.length; i++) {
            // console.log("zashlo", stack, res)
            while (stack && stack.length > 0 && temperatures[i] > stack[stack.length - 1][1]) {
                const pair = stack.pop();
                res[pair[0]] = i - pair[0];
            }
            stack.push([i, temperatures[i]])
        }
        return res;
    }
}
