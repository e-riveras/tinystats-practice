"""Summary statistics for a list of numbers."""


def mean(values):
    """Return the arithmetic mean of a list of numbers.

    Parameters
    ----------
    values : list of int or float
        The numbers. The list must not be empty.

    Returns
    -------
    float
        The mean of ``values``.

    Raises
    ------
    ValueError
        If ``values`` is empty.

    Examples
    --------
    >>> mean([1, 2, 3])
    2.0
    """
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values):

    sorted_num = sorted(values)
    n = len(sorted_num)
    mid = n // 2

    return mid
