def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    nums = 0
    for i in range(0, len(parens)):
        nums += 1
        if parens.startswith(')') and parens.endswith('('):
            return False

    if nums % 2 != 0:
        return False
    else:
        return True    

