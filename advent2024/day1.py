def read_input(filename):
    first_numbers = []
    second_numbers = []
    
    with open(filename, 'r') as file:
        for line in file:
            num1, num2 = line.strip().split()  # split on whitespace
            first_numbers.append(int(num1))
            second_numbers.append(int(num2))
    
    return first_numbers, second_numbers

def calculate_total_distance(list1, list2):
    # Sort both lists in ascending order
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    total = 0
    for num1, num2 in zip(list1, list2):
        # Calculate absolute difference between numbers
        distance = abs(num1 - num2)
        total += distance
    return total

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    # Convert right list to a dictionary counting occurrences
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # For each number in left list, multiply by its count in right list
    for num in left_list:
        count_in_right = right_counts.get(num, 0)  # get count (0 if not found)
        score = num * count_in_right
        total_score += score
    
    return total_score

# Read the input
first_list, second_list = read_input('lists.txt')

# Calculate and print both scores
distance_score = calculate_total_distance(first_list, second_list)
similarity_score = calculate_similarity_score(first_list, second_list)

print("Total distance:", distance_score)
print("Similarity score:", similarity_score)

