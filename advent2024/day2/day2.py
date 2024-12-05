def read_input():
    with open('input.txt', 'r') as file:
        # Read lines, strip whitespace, and split into lists of numbers
        lines = [line.strip().split() for line in file.readlines()]
        # Convert string numbers to integers
        number_lists = [[int(num) for num in line] for line in lines]
        print(number_lists)
    return number_lists

def check_sequence_with_skip(sequence):
    # Try removing each number one at a time
    for skip_index in range(len(sequence)):
        # Create new sequence without current number
        test_sequence = sequence[:skip_index] + sequence[skip_index + 1:]
        
        increasing = False
        decreasing = False
        invalid_change = False
        
        # Check sequence with skipped number
        for j in range(len(test_sequence)-1):
            difference = abs(test_sequence[j] - test_sequence[j+1])
            if difference > 3 or difference < 1:
                invalid_change = True
                break
                
            if test_sequence[j] < test_sequence[j+1]:
                increasing = True
            if test_sequence[j] > test_sequence[j+1]:
                decreasing = True
        
        # If this version is safe, return True
        if not (increasing and decreasing) and not invalid_change:
            print(f"Sequence becomes safe by removing {sequence[skip_index]}: {test_sequence}")
            return True
            
    return False

def check_sequence_safety(number_lists):
    unsafe_lists = []
    safe_lists = []
    
    for i, sequence in enumerate(number_lists):
        increasing = False
        decreasing = False
        invalid_change = False
        
        # Original safety check
        for j in range(len(sequence)-1):
            difference = abs(sequence[j] - sequence[j+1])
            if difference > 3 or difference < 1:
                invalid_change = True
                
            if sequence[j] < sequence[j+1]:
                increasing = True
            if sequence[j] > sequence[j+1]:
                decreasing = True
        
        # Initial safety determination        
        if (increasing and decreasing) or invalid_change:
            # Check if removing one number makes it safe
            if check_sequence_with_skip(sequence):
                safe_lists.append(sequence)
                print(f"List {i} is safe (after tolerating one bad number): {sequence}")
            else:
                unsafe_lists.append(sequence)
                print(f"List {i} is unsafe (cannot be fixed with one skip): {sequence}")
        else:
            safe_lists.append(sequence)
            pattern = "increasing" if increasing else "decreasing" if decreasing else "constant"
            print(f"List {i} is safe ({pattern}): {sequence}")
    
    return safe_lists, unsafe_lists

# Read and store the input
game_data = read_input()
safe_sequences, unsafe_sequences = check_sequence_safety(game_data)
print(f"\nFinal Results:")
print(f"Safe sequences found: {len(safe_sequences)}")
print(f"Unsafe sequences found: {len(unsafe_sequences)}")
