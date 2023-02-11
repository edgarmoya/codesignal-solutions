Given a string, find out if its characters can be rearranged to form a [palindrome](keyword://palindrome).

Example

For `inputString = "aabb"`, the output should be  
`solution(inputString) = true`.

We can rearrange `"aabb"` to make `"abba"`, which is a palindrome.

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] string inputString**
    
    A string consisting of lowercase English letters.
    
    _Guaranteed constraints:_  
    `1 ≤ inputString.length ≤ 50`.
    
-   **[output] boolean**
    
    `true` if the characters of the `inputString` can be rearranged to form a palindrome, `false` otherwise.