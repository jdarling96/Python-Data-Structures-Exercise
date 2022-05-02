def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_list = []
    for el in lst:
        if bool(el) == True:
            new_list.append(el)
    return new_list        