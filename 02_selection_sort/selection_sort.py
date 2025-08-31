# Finds the smallest value in an array
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Sort array
# O(n2)
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print(arr)

    newArr = selectionSort(arr)
    print(selectionSort(newArr))
