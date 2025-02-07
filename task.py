import random
import timeit

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


# Test functions
def test_merge_sort(arr):
    return merge_sort(arr.copy())

def test_insertion_sort(arr):
    return insertion_sort(arr.copy())

def test_timsort(arr):
    return sorted(arr)


def main():
    dataset_sizes = [10, 100, 1000, 10000] # розміри списків для сортування
    repetitions = 3  # кількість проходів для середнього арифметичного

    for size in dataset_sizes:
        data = [random.randint(0, size) for _ in range(size)]
        print(f"Dataset size   : {size}")

        merge_time = timeit.timeit(lambda: test_merge_sort(data), number=repetitions) / repetitions
        print(f"Merge Sort     : {merge_time:.6f}")

        insertion_time = timeit.timeit(lambda: test_insertion_sort(data), number=repetitions) / repetitions
        print(f"Insertion Sort : {insertion_time:.6f}")

        timsort_time = timeit.timeit(lambda: test_timsort(data), number=repetitions) / repetitions
        print(f"Timsort        : {timsort_time:.6f}")

        print("-" * 30)

if __name__ == '__main__':
    main()