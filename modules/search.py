def search_element (element, matrix, m, n):
    i = 0
    event = 0
    for i in range(m):
        j = 0
        for j in range(n):
            if element == matrix[i][j]:
                event = event + 1
    return event
