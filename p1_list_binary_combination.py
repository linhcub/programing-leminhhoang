def list_binary_combination(n):
    currentCombination = [0] * n

    i = 1
    total = 2**n
    while (i <= total):
        print(currentCombination)
        i = i + 1
        j = n - 1
        while (j >= 0):
            if currentCombination[j] == 1:
                currentCombination[j] = 0
            else:
                currentCombination[j] = 1
                break
            j = j - 1


list_binary_combination(15)
