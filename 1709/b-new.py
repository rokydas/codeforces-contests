n, m = [int(x) for x in input().split()]

heights = [int(x) for x in input().split()]
values = []

for i in range(len(heights) - 1):
    if heights[i] > heights[i+1]:
        values.append(heights[i] - heights[i+1])
    else:
        values.append(0)

cValues = [0]
cCount = 0
for j in range(len(values)):
    cValues.append(cCount + values[j])
    cCount += values[j]

valuesNeg = []
for i in range(len(heights) - 1, 0, -1):
    if heights[i] > heights[i-1]:
        valuesNeg.append(heights[i] - heights[i-1])
    else:
        valuesNeg.append(0)

cValuesNeg = [0]
cCount = 0
for j in range(len(values)):
    cValuesNeg.append(cCount + valuesNeg[j])
    cCount += valuesNeg[j]

for _ in range(m):
    x, y = [int(x) for x in input().split()]
    if x > y:
        print(cValuesNeg[n-y] - cValuesNeg[n-x])
    else:
        print(cValues[y-1] - cValues[x-1])
