# This program performs bitwise operations (AND, OR, XOR) on two input bit strings of equal length. 
# It validates the input, converts the strings to integers, performs the operations, and displays the results as bit strings.


a = input("Enter the first bit string: ")
b = input("Enter the second bit string: ")

# Step 2: Validate the input to ensure they are valid bit strings
if not (a.isdigit() and b.isdigit() and set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'})):
    print("Error: Please enter valid bit strings containing only 0s and 1s.")
elif len(a) != len(b):
    print("Error: The bit strings must be of equal length.")
else:
    # Step 3: Convert bit strings to integers
    a_int = int(a, 2)
    b_int = int(b, 2)

    # Step 4: Perform bitwise operations
    and_result = a_int & b_int
    or_result = a_int | b_int
    xor_result = a_int ^ b_int

    # Step 5: Convert results back to bit strings and pad with leading zeros to match the length
    bit_length = len(a)  # Length of the original bit strings
    and_result_str = bin(and_result)[2:].zfill(bit_length)
    or_result_str = bin(or_result)[2:].zfill(bit_length)
    xor_result_str = bin(xor_result)[2:].zfill(bit_length)

    # Step 6: Print the results
    print(f"AND: {and_result_str}")
    print(f"OR: {or_result_str}")
    print(f"XOR: {xor_result_str}")
