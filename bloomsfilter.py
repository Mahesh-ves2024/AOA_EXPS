# 10 Bloom Filter

size = 10
bloom = [0] * size

words = ["cat", "dog"]

for word in words:
    index = len(word) % size
    bloom[index] = 1

check = "cat"
index = len(check) % size

if bloom[index] == 1:
    print("May be present")
else:
    print("Not present")
