class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        prev = 0
        for operation in operations:
            if operation == "+":
                stack.append(int(stack[-2])+int(stack[-1]))
            elif operation == "D":
                stack.append(int(stack[-1])*2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)