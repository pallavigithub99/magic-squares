import numpy as np

def is_magic(A):
    """True if all line sums of A are equal."""
    target = A[0].sum()
    sums = A.sum(axis=0).tolist() + A.sum(axis=1).tolist()
    sums.append(A.trace())
    sums.append(np.fliplr(A).trace())
    return all(s == target for s in sums)

print(is_magic(np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])))
print(is_magic(np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]])))
print(is_magic(np.array([[16, 3, 2, 13], [5, 10, 11, 8],
                         [9, 6, 7, 12], [4, 15, 14, 1]])))
