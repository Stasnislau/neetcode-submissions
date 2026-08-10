class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let end = s.length - 1
        let begin = 0
        while (end > begin) {
            if (!this.isAlphanumeric(s[end])) {
                end--;
                continue;
            }
            if (!this.isAlphanumeric(s[begin])) {
                begin++;
                continue;
            }
            if (s[end].toLocaleLowerCase() !== s[begin].toLocaleLowerCase()) {
                console.log(s[end], s[begin])
                return false;
            }
            end--;
            begin++;
        }
        return true;
    }


    isAlphanumeric(char) {
        return (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z') ||
            (char >= '0' && char <= '9');
    }
}
