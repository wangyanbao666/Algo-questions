# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    half=[]
    for i, next in enumerate(text):
        if len(text)==1:
            return 1
        else:
            if next in "([{":
                # Process opening bracket, write your code here
                opening_brackets_stack.append(next)
                half.append(i)

            if next in ")]}":
                # Process closing bracket, write your code here
                if len(opening_brackets_stack)==0:
                    return i+1
                else:
                    if next==')' and opening_brackets_stack[-1]!='(' or \
                        next == ']' and opening_brackets_stack[-1] != '[' or \
                        next == '}' and opening_brackets_stack[-1] != '{':
                        return i+1
                    opening_brackets_stack.pop()
                    half.pop()
    if len(opening_brackets_stack)!=0:
        return half[0]+1
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
