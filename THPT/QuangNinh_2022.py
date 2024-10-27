# Bài 1

"""
n = int(input())
arr = list(map(int, input().split()))
newArr = list(map(int, input().split()))

s1 = sum(arr)
s2 = sum(newArr)
m = len(newArr)

minElement = -1 # là giá trị không bao giờ xảy ra.
for i in range(len(arr)):
    # Giả sử i không được thêm giá trị
    k = s2 - s1 + arr[i]
    
    if k % m == 0:
        flag = False
        for j in range(len(arr)):
            if j != i:
                x = arr[j] + k // m
                #print(x)
                if x not in newArr:
                    flag = True
                    break
        if flag == False or min == -1 or (min != -1 and min < k // m):
            min = k // m
            break
        
"""

# Bài 2
"""
s1 = input()
s2 = input()

lenList = []

for i in range(1, len(s2)):
    p1 = s1.find(s2[i-1])
    p2 = s1.rfind(s2[i])
    lenList.append(p2-p1)
print(lenList)
"""

# Bài 3
"""
result = []
def backtrack(arr, newArr, index, total):
    #print(total)
    global result
    if total == 10:
        result.append(newArr.copy())
        return
    if total > 10:
        return
    if index >= len(arr):
        return

    newArr.append(arr[index])
    backtrack(arr, newArr, index+1, total + arr[index])
    newArr.pop()

    backtrack(arr, newArr, index+1, total)

arr = [4, 7, 5, 1, 3]

backtrack(arr, [], 0, 0)
print(result)
"""

