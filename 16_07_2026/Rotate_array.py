"""Given an array arr, rotate the array by one position in clockwise direction."""
arr=[9, 8, 7, 6, 4, 2, 1, 3]
arr[:]=arr[-1:]+arr[:-1]
print(arr)