def yield_slices(lst, slice_size):
    for i in range(0, len(lst), slice_size):
        yield lst[i: i + slice_size]

# Example usage:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for slice in yield_slices(lst, 3):
    print(slice)
