#Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

#Example

#For inputArray = [-2, 2, 5, -11, 6], the output should be arrayMaxConsecutiveSum2(inputArray) = 7.

#The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.integer inputArray

#An array of integers.

#Guaranteed constraints:
#3 ≤ inputArray.length ≤ 10**5,
#-1000 ≤ inputArray[i] ≤ 1000.

#[output] integer

#The maximum possible sum of a subarray within inputArray.

def arrayMaxConsecutiveSum2(inputArray):
    currmax, m = inputArray[0], inputArray[0]
    for i in range(1, len(inputArray)):
        currmax = max(inputArray[i], currmax + inputArray[i])
        m = max(currmax, m)
    return m
