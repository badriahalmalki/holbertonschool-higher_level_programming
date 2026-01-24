#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices after validating inputs."""

    # Validate m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    # Validate m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    # Validate m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a not empty ([], [[]], or any row empty)
    if m_a == [] or m_a == [[]] or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    # Validate m_b not empty ([], [[]], or any row empty)
    if m_b == [] or m_b == [[]] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Validate all elements of m_a are int or float
    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Validate all elements of m_b are int or float
    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Validate each row of m_a is of the same size
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    # Validate each row of m_b is of the same size
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(row_len_b):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            result_row.append(s)
        result.append(result_row)

    return result
