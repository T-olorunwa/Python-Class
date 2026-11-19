# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Copmpute and print the union of set1 and set2
X = set1.union(set2) #I can also use set1 | set2
print(X)

# Copmpute and print the intersection of set1 and set2
A = set1.intersection(set2) #I can also use set1 & set2
print(A)

# Copmpute and print the difference between set1 and set2
B = set1 - set2 #I can also use set1.difference(set2)
print(B)

# Copmpute and print the symmetric difference between set1 and set2
C = set1 ^ set2 #I can also use set1.symmetric_difference(set2)
print(C)
