class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length)
            return false;

        let firstSorted = s.split('').sort().join('');
        let secondSorted = t.split('').sort().join('');

        return (firstSorted.indexOf(secondSorted) !== -1);
    }
}