class BinarySearch():

    def search_iterative(self, list, item):
        # low and high keep track of part of the list to search in
        low = 0
        high = len(list) - 1

        # While you haven't narrow it down to one element...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = list[mid]
            # Found element
            if guess == item:
                return mid
            # The guess is too high
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        # Doesn't exist
        return None






if __name__ == '__main__':
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3)) # => 1
    
    print(bs.search_iterative(my_list, -1)) # => None
