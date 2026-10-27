# nums=[2,3,4,5,9,8,7,6,1]
# print(nums)
# nums.sort()
# print(nums)


# bubble sort
# nums=[2,3,4,5,9,8,7,6,1]
# print(nums)
# n=len(nums)

# for i in range(n):
#     for j in range(n-1-i):
#         if nums[j]>nums[j+1]:
#             temp=nums[j]
#             nums[j]=nums[j+1]
#             nums[j+1]=temp

# print(nums)


# insertion sort
# nums=[2,3,4,5,9,8,7,6,1]
# print(nums)
# n=len(nums)

# for i in range(1,n):
#     key =nums[i]
#     j=i-1
#     while j>=0 and nums[j]>key:
#         nums[j+1]=nums[j]
#         j-=1
#     nums[j+1]=key

# print(nums)


#selection sort
# nums=[2,3,4,5,9,8,7,6,1]
# print(nums)
# n=len(nums)

# for i in range(n):
#     mn=nums[i]
#     ind=i
#     for j in range(i+1,n):
#         if nums[j]<mn:
#             mn=nums[j]
#             ind=j

#     temp=nums[i]
#     nums[i]=nums[ind]
#     nums[ind]=temp
# print(nums)

#merge sort

def merge(nums, l, mid, r):
    a = []
    b = []
    
    for i in range(l, mid + 1):
        a.append(nums[i])
    for i in range(mid + 1, r + 1):
        b.append(nums[i])   

    i, j, k = 0, 0, l

    while k <= r:
        if j == len(b):
            nums[k] = a[i]
            i += 1
        elif i == len(a):
            nums[k] = b[j]
            j += 1
        elif a[i] < b[j]:
            nums[k] = a[i]
            i += 1
        else:
            nums[k] = b[j]
            j += 1
        k += 1   # cleaner increment

def mergesort(nums, l, r):
    if l >= r:
        return
    
    mid = (l + r) // 2
    mergesort(nums, l, mid)
    mergesort(nums, mid + 1, r)

    merge(nums, l, mid, r)

def sortArray(nums):
    mergesort(nums, 0, len(nums) - 1)
    return nums

nums = [2,3,4,5,9,8,7,6,1]
print(nums)
print(sortArray(nums))
