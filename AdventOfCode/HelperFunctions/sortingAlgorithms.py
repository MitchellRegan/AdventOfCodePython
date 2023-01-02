#Fun visual guide to these algorithms: https://imgur.com/gallery/voutF

#https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Bubble Sort
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
def coctail_shaker_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Coctail Shaker Sort
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
def insertion_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Insertion Sort
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
def shell_sort(li, greaterThan=(lambda a,b: a>b), gapSequence=[5,3,1]):
    '''Shell Sort
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
def comb_sort(li, greaterThan=(lambda a,b: a>b), shrinkFactor=1.3):
    '''Comb Sort
    Performance: O(n^2 / 2^p) where 'p' is the number of increments
    Space: O(1)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
        shrinkFactor: The amount to divide the gap size by in each iteration.
    '''
    gap = len(li)
    while True:
        gap = int(gap / shrinkFactor)
        if gap < 1:
            return

        i = 0
        while i + gap < len(li):
            if greaterThan(li[i], li[i+gap]):
                placeholder = li[i]
                li[i] = li[i+gap]
                li[i+gap] = placeholder
            i += 1


#https://en.wikipedia.org/wiki/Merge_sort
def merge_sort_top_down(li, greaterThan=(lambda a,b: a>b)):
    '''Top-Down, Recursive Merge Sort
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
def selection_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Selection Sort
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
def heap_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Heap Sort
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''
    #Turn the list into a max heap

    return


#https://en.wikipedia.org/wiki/Quicksort
def quick_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Quick Sort
    Performance: O(n log(n))
    Space: O(n)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''

    return


#https://en.wikipedia.org/wiki/Radix_sort
def radix_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Radix Sort
    Performance: O(w*n)
    Space: O(w+n)
        Note: w = key length and n = number of keys
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''

    return


#https://en.wikipedia.org/wiki/Bitonic_sorter
def bitonic_sort(li, greaterThan=(lambda a,b: a>b)):
    '''Bitonic Sort
    Performance: O(log(n)^2) parallel time
    Space: O(n log(n)^2)
    Params:
        li: The list to be sorted.
        greaterThan: lambda function to check if one value is greater than another. Defaults to "a>b"
    '''

    return