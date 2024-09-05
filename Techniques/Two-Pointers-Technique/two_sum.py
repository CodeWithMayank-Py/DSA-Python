def twosum(arr,n,x):
    i = 0           # First Pointer
    j = n - 1       # Second Pointer
    
    while i<j:
        
        if arr[i] + arr[j] == x:    # Check if the sume of pointers position is equal to X
            return (arr[i], arr[j])     # Return the pair of number that is equal to X
        
        elif arr[i] + arr[j] > x:   # If sum is greater than X, move right pointer towards left 
            j -= 1      # Move pointers towards left
        
        else:       # If sum is smaller than X, move pointer left pointer towards right
            i += 1  # Move first pointer towards right
    
    return False

if __name__ == '__main__':
    arr = [5,8,9,10]   # Given Array
    x = 17          # Target Number
    n = len(arr)    # Returns the length of the array
    arr.sort()      # If array is not sorted
    print(twosum(arr,n,x)) # Print the pairs of targeted number in array
    # Output: (8,9)