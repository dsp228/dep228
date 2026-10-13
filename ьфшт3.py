

def merge_sorted_lists(list1, list2):
    combined = list1 + list2

    combined.sort()

    result = []
    for num in combined:
        if not result or num != result[-1]:
            result.append(num)

    return result


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

merged = merge_sorted_lists(list1, list2)

print(merged)
