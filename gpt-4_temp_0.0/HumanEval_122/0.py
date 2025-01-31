def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Initialize the sum to 0
    sum_of_elements = 0

    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the element has at most two digits
        if 0 <= abs(arr[i]) <= 99:
            # Add the element to the sum
            sum_of_elements += arr[i]

    # Return the sum of the elements
    return sum_of_elements