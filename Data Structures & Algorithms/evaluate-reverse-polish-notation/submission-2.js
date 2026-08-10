class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = new Array();
        const operators = ["+", "-", "*", "/"]
        for (let i = 0; i < tokens.length; i++) {
            if (operators.includes(tokens[i])) {
                const secondNumber = Number(stack.pop());
                const firstNumber = Number(stack.pop());
                let result = 0;
                switch (tokens[i]) {
                    case "+":
                        result = firstNumber + secondNumber;
                        break;
                    case "-":
                        result = firstNumber - secondNumber;
                        break;
                    case "*":
                        result = firstNumber * secondNumber;
                        break;
                    case "/":
                        result = Math.trunc(firstNumber / secondNumber);
                        break;
                    default:
                        break;
                }
                stack.push(result);
            }
            else {
                stack.push(tokens[i]);
            }
        }
        return stack.pop();
    }
}
