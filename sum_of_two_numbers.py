lon = [1, -1, 2, 3, 4, 11, 8]  # Length of numbers


#       O(n**2), O(n)        (Time complexity, Space complexity)
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(len(array)):
#             secondSum = array[j]
#             if firstNum + secondSum == targetSum:
#                 return [firstNum, secondSum]
#     return []


#       O(n), O(n)           (Time complexity, Space complexity)
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         sum = targetSum - num
#         if sum in nums:
#             return [sum, num]
#         else:
#             nums[num] = True
#     return []


#       O(nlogn), O(1)           (Time complexity, Space complexity)
# def twoNumberSum(array, targetSum):
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         currentSum = array[left] + array[right]
#         if currentSum == targetSum:
#             return [array[left], array[right]]
#         elif currentSum > targetSum:
#             right -= 1
#         elif currentSum < targetSum:
#             left += 1
#     return []


print(twoNumberSum(lon, 10))
