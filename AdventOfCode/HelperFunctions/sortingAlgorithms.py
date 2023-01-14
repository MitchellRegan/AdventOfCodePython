#Fun visual guide to these algorithms: https://imgur.com/gallery/voutF

#https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(li):
    '''Bubble Sort
    Performance: O(n^2)
    Space: O(n)
    Params:
        li: The list to be sorted.
    '''
    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                placeholder = li[i]
                li[i] = li[j]
                li[j] = placeholder


def bubble_sort_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Bubble Sort for complex objects that require a custom comparitor.
    Performance: O(n^2)
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):
            if greaterThan(li[i], li[j]):
                placeholder = li[i]
                li[i] = li[j]
                li[j] = placeholder



#https://en.wikipedia.org/wiki/Cocktail_shaker_sort
def coctail_shaker_sort(li):
    '''Coctail Shaker Sort
    Performance: O(n^2)
    Space: O(1)
    Params:
        li: The list to be sorted.
    '''
    min = 0
    max = len(li)-1
    while True:
        swapped = False
        for i in range(min, max):
            if li[i] > li[i+1]:
                placeholder = li[i]
                li[i] = li[i+1]
                li[i+1] = placeholder
                swapped = True

        if not swapped:
            return
        else:
            max -= 1

        for i in range(max, min, -1):
            if li[i-1] > li[i]:
                placeholder = li[i]
                li[i] = li[i-1]
                li[i-1] = placeholder
                swapped = True

        if not swapped:
            return
        else:
            min += 1


def coctail_shaker_sort_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Coctail Shaker Sort for complex objects that require a custom comparitor.
    Performance: O(n^2)
    Space: O(1)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    min = 0
    max = len(li)-1
    while True:
        swapped = False
        for i in range(min, max):
            if greaterThan(li[i], li[i+1]):
                placeholder = li[i]
                li[i] = li[i+1]
                li[i+1] = placeholder
                swapped = True

        if not swapped:
            return
        else:
            max -= 1

        for i in range(max, min, -1):
            if greaterThan(li[i-1], li[i]):
                placeholder = li[i]
                li[i] = li[i-1]
                li[i-1] = placeholder
                swapped = True

        if not swapped:
            return
        else:
            min += 1



#https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(li):
    '''Insertion Sort
    Performance: O(n^2)
    Space: O(n)
    Params:
        li: The list to be sorted.
    '''
    for i in range(1, len(li)):
        j = i
        while j > 0 and li[j-1] > li[j]:
            placeholder = li[j]
            li[j] = li[j-1]
            li[j-1] = placeholder
            j -= 1


def insertion_sort_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Insertion Sort for complex objects that require a custom comparitor.
    Performance: O(n^2)
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    for i in range(1, len(li)):
        j = i
        while j > 0 and greaterThan(li[j-1], li[j]):
            placeholder = li[j]
            li[j] = li[j-1]
            li[j-1] = placeholder
            j -= 1



#https://en.wikipedia.org/wiki/Shellsort
def shell_sort(li, gapSequence=[5,3,1]):
    '''Shell Sort
    Performance: between O(n^2) and O(n log(n)), based on gap sizes
    Space: O(n)
    Params:
        li: The list to be sorted.
        gapSequence: A list of decreasing ints that designate the index gap for each iteration. Defaults to [5,3,1]
    '''
    for gap in gapSequence:
        for i in range(gap, len(li)):
            j = i
            while j >= gap and li[j-gap] > li[j]:
                placeholder = li[j]
                li[j] = li[j-gap]
                li[j-gap] = placeholder
                j -= gap


def shell_sort_complex(li, greaterThan=(lambda a,b: a>b), gapSequence=[5,3,1]):
    '''Shell Sort for complex objects that require a custom comparitor.
    Performance: between O(n^2) and O(n log(n)), based on gap sizes
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: Lambda function to check if one value is greater than another. Defaults to "a>b"
        gapSequence: A list of decreasing ints that designate the index gap for each iteration. Defaults to [5,3,1]
    '''
    for gap in gapSequence:
        for i in range(gap, len(li)):
            j = i
            while j >= gap and greaterThan(li[j-gap], li[j]):
                placeholder = li[j]
                li[j] = li[j-gap]
                li[j-gap] = placeholder
                j -= gap



#https://en.wikipedia.org/wiki/Comb_sort
def comb_sort(li, shrinkFactor=1.3):
    '''Comb Sort
    Performance: O(n^2 / 2^p) where 'p' is the number of increments
    Space: O(1)
    Params:
        li: The list to be sorted.
        shrinkFactor: The amount to divide the gap size by in each iteration.
    '''
    gap = len(li)
    sorted = False
    while not sorted:
        gap = int(gap // shrinkFactor)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(li) - gap):
            if li[i] > li[gap+i]:
                placeholder = li[i]
                li[i] = li[gap+i]
                li[gap+i] = placeholder
                sorted = False


def comb_sort_complex(li, greaterThan=(lambda a,b: a>b), shrinkFactor=1.3):
    '''Comb Sort for complex objects that require a custom comparitor.
    Performance: O(n^2 / 2^p) where 'p' is the number of increments
    Space: O(1)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
        shrinkFactor: The amount to divide the gap size by in each iteration.
    '''
    gap = len(li)
    sorted = False
    while not sorted:
        gap = int(gap // shrinkFactor)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(li) - gap):
            if greaterThan(li[i], li[gap+i]):
                placeholder = li[i]
                li[i] = li[gap+i]
                li[gap+i] = placeholder
                sorted = False



#https://en.wikipedia.org/wiki/Merge_sort
def merge_sort_top_down(li):
    '''Top-Down, Recursive Merge Sort
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
    '''
    if len(li) <= 1:
        return li

    #Dividing the list into two, evenly-sized sublist
    split = int(len(li)//2)
    left = li[:split]
    right = li[split:]

    #Recursively sorting each sublist
    merge_sort_top_down(left)
    merge_sort_top_down(right)

    #Merging the sorted sublists
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            li[l+r] = right[r]
            r += 1
        else:
            li[l+r] = left[l]
            l += 1
    while l < len(left):
        li[l+r] = left[l]
        l += 1
    while r < len(right):
        li[l+r] = right[r]
        r += 1


def merge_sort_top_down_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Top-Down, Recursive Merge Sort for complex objects that require a custom comparitor.
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    if len(li) <= 1:
        return li

    #Dividing the list into two, evenly-sized sublist
    split = int(len(li)//2)
    left = li[:split]
    right = li[split:]

    #Recursively sorting each sublist
    merge_sort_top_down(left, greaterThan)
    merge_sort_top_down(right, greaterThan)

    #Merging the sorted sublists
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if greaterThan(left[l], right[r]):
            li[l+r] = right[r]
            r += 1
        else:
            li[l+r] = left[l]
            l += 1
    while l < len(left):
        li[l+r] = left[l]
        l += 1
    while r < len(right):
        li[l+r] = right[r]
        r += 1



#https://en.wikipedia.org/wiki/Selection_sort
def selection_sort(li):
    '''Selection Sort
    Performance: O(n^2)
    Space: O(1)
    Params:
        li: The list to be sorted.
    '''
    for i in range(len(li)-1):
        min = i
        for j in range(i+1, len(li)):
            if li[min] > li[j]:
                min = j
        placeholder = li[min]
        li[min] = li[i]
        li[i] = placeholder


def selection_sort_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Selection Sort for complex objects that require a custom comparitor.
    Performance: O(n^2)
    Space: O(1)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    for i in range(len(li)-1):
        min = i
        for j in range(i+1, len(li)):
            if greaterThan(li[min], li[j]):
                min = j
        placeholder = li[min]
        li[min] = li[i]
        li[i] = placeholder



#https://en.wikipedia.org/wiki/Heapsort
def heap_sort(li):
    '''Heap Sort
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
    '''
    #Convert the list to a binary max heap in-place, starting from the last element and working backwards
    for i in range(len(li)-1, -1, -1):
        root = i
        while (root * 2) + 1 < len(li):
            left = (root * 2) + 1
            swap = root

            if li[swap] < li[left]:
                swap = left
            if left+1 < len(li) and li[swap] < li[left+1]:
                swap = left + 1
            if swap == root:
                break
            placeholder = li[root]
            li[root] = li[swap]
            li[swap] = placeholder
            root = swap

    #Loop where the largest (root) element of the heap is placed at the end of the list
    for last in range(len(li)-1, 0, -1):
        placeholder = li[last]
        li[last] = li[0]
        li[0] = placeholder
        #Sifting the root element down to get the new largest value at the top
        root = 0
        while (root * 2) + 1 <= last-1:
            left = (root * 2) + 1
            swap = root

            if li[swap] < li[left]:
                swap = left
            if left+1 <= last-1 and li[swap] < li[left+1]:
                swap = left + 1
            if swap == root:
                break
            placeholder = li[root]
            li[root] = li[swap]
            li[swap] = placeholder
            root = swap


def heap_sort_complex(li, lessThan=(lambda a,b: a<b)):
    '''Heap Sort for complex objects that require a custom comparitor.
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        lessThan: lambda function to check if one value is smaller than another. Defaults to "a<b"
    '''
    #Convert the list to a binary max heap in-place, starting from the last element and working backwards
    for i in range(len(li)-1, -1, -1):
        root = i
        while (root * 2) + 1 < len(li):
            left = (root * 2) + 1
            swap = root

            if lessThan(li[swap], li[left]):
                swap = left
            if left+1 < len(li) and lessThan(li[swap], li[left+1]):
                swap = left + 1
            if swap == root:
                break
            placeholder = li[root]
            li[root] = li[swap]
            li[swap] = placeholder
            root = swap

    #Loop where the largest (root) element of the heap is placed at the end of the list
    for last in range(len(li)-1, 0, -1):
        placeholder = li[last]
        li[last] = li[0]
        li[0] = placeholder
        #Sifting the root element down to get the new largest value at the top
        root = 0
        while (root * 2) + 1 <= last-1:
            left = (root * 2) + 1
            swap = root

            if lessThan(li[swap], li[left]):
                swap = left
            if left+1 <= last-1 and lessThan(li[swap], li[left+1]):
                swap = left + 1
            if swap == root:
                break
            placeholder = li[root]
            li[root] = li[swap]
            li[swap] = placeholder
            root = swap



#https://en.wikipedia.org/wiki/Quicksort
def quick_sort(li, left, right):
    '''Quick Sort
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        left: The left-most index in the list partition to sort.
        right: The right-most index in the list partition to sort.
    '''
    #Must have at least 2 elements in the partition to sort
    if left >= right or left < 0:
        return

    tempPivot = left - 1
    #Comparing each element in the list partition to the element at the pivot index (we're using the right-most index as the pivot)
    for i in range(left, right):
        if li[i] <= li[right]:
            tempPivot += 1
            placeholder = li[i]
            li[i] = li[tempPivot]
            li[tempPivot] = placeholder

    tempPivot += 1
    placeholder = li[tempPivot]
    li[tempPivot] = li[right]
    li[right] = placeholder
    
    #Recursively calling sorting all elements to the left, and all elements to the right of our temp pivot
    quick_sort(li, left, tempPivot-1)
    quick_sort(li, tempPivot+1, right)


def quick_sort_complex(li, left, right, greaterThan=(lambda a,b: a>b)):
    '''Quick Sort for complex objects that require a custom comparitor.
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        left: The left-most index in the list partition to sort.
        right: The right-most index in the list partition to sort.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    #Must have at least 2 elements in the partition to sort
    if left >= right or left < 0:
        return

    tempPivot = left - 1
    #Comparing each element in the list partition to the element at the pivot index (we're using the right-most index as the pivot)
    for i in range(left, right):
        if greaterThan(li[right], li[i]):
            tempPivot += 1
            placeholder = li[i]
            li[i] = li[tempPivot]
            li[tempPivot] = placeholder

    tempPivot += 1
    placeholder = li[tempPivot]
    li[tempPivot] = li[right]
    li[right] = placeholder
    
    #Recursively calling sorting all elements to the left, and all elements to the right of our temp pivot
    quick_sort_complex(li, left, tempPivot-1, greaterThan)
    quick_sort_complex(li, tempPivot+1, right, greaterThan)



#https://en.wikipedia.org/wiki/Radix_sort
def radix_sort_LSD(li):
    '''Least-Significant Digit Radix Sort
    Performance: O(w*n)
    Space: O(w+n)
        Note: w = element length and n = number of elements
    Params:
        li: The list to be sorted.
     '''

    return


def radix_sort_LSD_complex(li, greaterThan=(lambda a,b: a>b)):
    '''Least-Significant Digit Radix Sort for complex objects that require a custom comparitor.
    Performance: O(w*n)
    Space: O(w+n)
        Note: w = key length and n = number of keys
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''

    return



#https://en.wikipedia.org/wiki/Bitonic_sorter
def bitonic_sort(li):
    '''Bitonic Sort
    Performance: O(log(n)^2) parallel time
    Space: O(n log(n)^2)
    Params:
        li: The list to be sorted.
    '''

    return


def bitonic_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Bitonic Sort for complex objects that require a custom comparitor.
    Performance: O(log(n)^2) parallel time
    Space: O(n log(n)^2)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''

    return