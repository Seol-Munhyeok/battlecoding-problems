#PYTHON

names = ["A", "B", "C"]
scores = [80, 90, 100]
print(" | ".join([f"{n}:{s}" for n, s in zip(names, scores)]))

# 출력값 : A:80 | B:90 | C:100