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


