# ЮНУСОВ ПАВЕЛ ИИАД 1

def merge_sorted_lists(list1, list2):
    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        a = list1[i]
        b = list2[j]

        if a < b:
            if not merged or a != merged[-1]:
                merged.append(a)
            i += 1
        elif a > b:
            if not merged or b != merged[-1]:
                merged.append(b)
            j += 1
        else:  # a == b
            if not merged or a != merged[-1]:
                merged.append(a)
            i += 1
            j += 1

    while i < len(list1):
        a = list1[i]
        if not merged or a != merged[-1]:
            merged.append(a)
        i += 1
    while j < len(list2):
        b = list2[j]
        if not merged or b != merged[-1]:
            merged.append(b)
        j += 1
    return merged

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)  
