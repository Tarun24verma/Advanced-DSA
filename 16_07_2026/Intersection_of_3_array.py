"""Given three sorted arrays in non-decreasing order, return all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array.
Note: Ignore duplicates, include each common element only once in the output."""
a,b,c=[1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]
a = list(set(c).intersection(set(b).intersection(set(a))))
a.sort()
print(a)