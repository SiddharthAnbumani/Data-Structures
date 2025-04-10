def ValidParenthesis(s):
    stack = []
    mapping = {")":"(", "}": "{" , "]": "[" }
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                    return False
            stack.pop()
        else:
            continue
    return len(stack) == 0