# Binary Search - when we try to find a target in a sorted arr, we use binary search
# assign low=0, high=end of the list, find middle=(low+high)/2 then check the middle element
# if it's lesser or greater, if it's lesser than the target, then the target is in upper half of the 
# arr(low=middle+1), if greater, then, it's in lower half of the arr(high=middle-1)

# we put low <= high because of [5] case, while won't even start if low < high

# WHY WE ARE DOING START <= END (WHY =?)
# if the start lands on end and that is equal to the target, then start < end will terminate
# To avoid that, we put while low <= high

def binary_search(nums: list[int], target: int) -> int:
  low = 0
  high = len(nums) - 1
  while low <= high:
    middle = (low + high) // 2
    if nums[middle] == target:
      return middle
    if nums[middle] < target:
      low = middle + 1
    else:
      high = middle - 1
  return -1

# Call the test function
if __name__ == "__main__":
    print(binary_search([-1,0,3,5,9,12],9))