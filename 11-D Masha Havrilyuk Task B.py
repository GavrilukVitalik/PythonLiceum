def get_number_element(a, compare):
    elem = a[0]
    number_element = 1
    for counter in range(1, len(a), 1):
        if compare == '<' and a[counter] < elem:
            elem = a[counter]
            number_element = counter + 1
        elif compare == '>' and a[counter] >= elem:
            elem = a[counter]
            number_element = counter + 1
    return number_element


n = int(input())
k = 0
if n != 0:
    A = []
    s = input().split()
    error = False
    for i in range(n):
        d = int(s[i])
        A.append(d)
        if abs(d) > 100:
            error = True
    if not error:
        minElement = get_number_element(A, '<')
        maxElement = get_number_element(A, '>')
        if maxElement > minElement:
            i_start = minElement
            i_end = maxElement
        else:
            i_start = maxElement
            i_end = minElement
        while i_start <= i_end:
            if A[i_start - 1] < 0:
                k += 1
            i_start += 1
print(k)
