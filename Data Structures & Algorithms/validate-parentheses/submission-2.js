class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length % 2 !== 0)
            return false;
            
        let operationStack = [];
        for(let i=0; i < s.length; i++){
            let currentChar = s[i];
            let currentTop = operationStack[operationStack.length - 1];
            switch(currentChar){
                case '{':
                case '[':
                case '(':
                    operationStack.push(currentChar);
                    break;
                case '}':
                    if(!currentTop || currentTop !== '{')
                        return false; 
                    else 
                        operationStack.pop();
                    break;
                case ']':
                    if(!currentTop || currentTop !== '[')
                        return false; 
                    else 
                        operationStack.pop();
                    break;
                case ')':
                    if(!currentTop || currentTop !== '(')
                        return false; 
                    else 
                        operationStack.pop();
                    break;
                default:
                    break;
            }
        }

        return operationStack.length < 1;
    }
}
