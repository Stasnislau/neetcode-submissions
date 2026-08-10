class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;
        let begin = 0;
        let end = heights.length - 1;
        while (begin < end) {
            const distance = end - begin;
            const minValue = heights[begin] < heights[end] ? heights[begin] : heights[end];
            const area = minValue * distance
            if (max < area) {
                max = area;
            }
            if (heights[begin] < heights[end])
                begin++;
            else
                end--;
        }
        return max;
    }
}
