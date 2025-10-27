class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid_indices = set()
        stack = []
        result = ""
        for index in range(len(s)):
            if (s[index] == '('):
                stack.append(index)
            elif (s[index] == ')'):
                if (len(stack) == 0):
                    invalid_indices.add(index)
                else:
                    stack.pop()
        
        for element in stack:
            invalid_indices.add(element)
        
        for index in range(len(s)):
            if (index not in invalid_indices):
                result += s[index]
        return result


input = "))(("
soln = Solution()
result = soln.minRemoveToMakeValid(input)
print(result)