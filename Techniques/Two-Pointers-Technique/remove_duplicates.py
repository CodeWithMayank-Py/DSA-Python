# Problem: Removing Duplicates
# We have given an sorted array, we have to remove the duplicates,
# using 2 pointer approach and return the new array & length of the array
# Ex = [1,1,1,2,2,3,3,4,5,5,6]
# Output: [1,2,3,4,5,6], new length = 6


# Approach
# Since the array is sorted, so duplicates elements will be next to each other
# So we can initialize our first pointer at 0, i.e. i=0
# And we iterate with 'j' from the range of 1 to n-1
# at each iteration we match the arr[j] != arr[i], if the i and j values match we will move
# next, and if the next iteration doesn't match with arr[i], we will increment the i and 
# overwrite the element with the unique element.
# We are not deleting or shifting the elements we are overwriting the elements

# Code Implementation

def removeduplicates(arr):
    # Checks if the arr is empty or not
    if not arr:
        return 0
    
    # First pointer to track the unique elements
    i=0
    
    # 'j' pointer will iterate from 1 to n-1 range
    for j in range(1, len(arr)):
        # Checks the element, is it duplicate or not
        if arr[j] != arr[i]:
            i += 1      # If element is not duplicate, we will increment the i with +1, so our unique element tracker can be placed at its new position
            arr[i] = arr[j]     # Overwrites the element, previous our unique element is at 0 position
            # after increment of i with 1, we overwrite the arr[1] with arr[j].
            # Now arr[1] has tracker pointer.
        
    return i+1      # Returns the length of the new array



# Driver's code
if __name__ == '__main__':
    arr = [1,1,1,1,2,2,2,3,4,5,5,5,6,6]
    new_length = removeduplicates(arr)
    print(f"New array: {arr[:new_length]}")     # It returns 6, we use the slicing method to print arr
    print(f"Length of the array: {new_length}")     # 6
    

# Time Complexity
# O(n), we use the for loop once

# Space Complexity
# O(1), since no extra space needed except for two pointers