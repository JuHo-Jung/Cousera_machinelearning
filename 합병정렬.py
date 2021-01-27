#Merge 정렬

def merge(lst, temp, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high+1):
        if i > mid:
            temp[k] = lst[j]
            j += 1
        elif j > high:
            temp[k] = lst[i]
            i += 1
        elif lst[j] < lst[i]:
            temp[k] = lst[j]
            j += 1
        else:
            temp[k] = lst[i]
            i += 1
    for k in range(low, high+1):
        lst[k] = temp[k]

def merge_sort(lst, temp, low, high):
    if high <= low:
        return None
    mid = low + (high - low)// 2
    merge_sort(lst, temp, low, mid)
    merge_sort(lst, temp, mid+1, high)
    merge(lst, temp, low, mid, high)
