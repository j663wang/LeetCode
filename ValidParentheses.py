# Code for Valid Parentheses #20
# Problem:
#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#  An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.


# Input:
#       s: string of parentheses
# Return:
#       true if string is valid
#       false if string is invalid
def valid_parenth(s: str) -> bool:
    parenth_lst = []
    for single_parenth in s:
        if single_parenth in ['(', '{', '[']:
            parenth_lst.append(single_parenth)
        else:
            if len(parenth_lst) == 0:
                return False
            last_l_parenth = parenth_lst.pop()
            if single_parenth == ')' and last_l_parenth != '(':
                return False
            elif single_parenth == '}' and last_l_parenth != '{':
                return False
            elif single_parenth == ']' and last_l_parenth != '[':
                return False
    if len(parenth_lst) == 0:
        return True
    else:
        return False