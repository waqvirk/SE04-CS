### Valid Parentheses ###
def is_valid(s: str) -> bool:
    stack = []      # use like a stack
    pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for ch in s:
        if ch in "([{":      #if it's an opening bracket
            stack.append(ch)
        else:        # must be a closing bracket
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False
    return not stack

# Examples
s = "()"
print()
print("String 's' composed only of the characters:", s)
print("Is bracket arrangement in this string valid?:", is_valid(s))
print("-"*51)

s = "()[]{}"
print("String 's' composed only of the characters:", s)
print("Is bracket arrangement in this string valid?:", is_valid(s))
print("-"*51)

s = "(]"
print("String 's' composed only of the characters:", s)
print("Is bracket arrangement in this string valid?:", is_valid(s))
print("-"*51)

s = "([])"
print("String 's' composed only of the characters:", s)
print("Is bracket arrangement in this string valid?:", is_valid(s))
print("-"*51)

