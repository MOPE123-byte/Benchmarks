def insertion_sort(L):
    for num in range(1, len(L)):
        key = L[num]
        j = num - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

# Example usage:
my_list = [5, 2, 9, 1, 34, 6]
insertion_sort(my_list)
print(my_list)

a = [3,5,4,8,6,9]


