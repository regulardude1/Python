def binary_search(arr, target, low, high):
    # If the range is invalid, the target is not in the list
    if low > high:
        return -1
    
    # Calculate the middle index
    mid = (low + high) // 2
    
    # Check if the middle element is the target
    if arr[mid] == target:
        return mid
    # If the target is smaller, search the left half
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # If the target is larger, search the right half
    else:
        return binary_search(arr, target, mid + 1, high)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    
    while True:
        try:
            # Asking the user for the number to search for
            target = int(input('What number would you like to search for?\n'))
            
            result = binary_search(arr, target, 0, len(arr) - 1)

            print(f"Target found at index: {result}" if result != -1 else "Target not found")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  

          # Ask user if they want to search for another number
        while True:
            again = input('Would you like to search for another number? (yes/no)\n').strip().lower()
            if again == 'yes':
                break  
            elif again == 'no':
                print("Thank you for running this program.")
                return  
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue  

if __name__ == "__main__":
    main()
