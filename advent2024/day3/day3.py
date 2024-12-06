import re

def solve_mul_instructions(filename):

    with open(filename, 'r') as file:
        content = file.read()
    
    pattern = r'(?:do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
    matches = re.finditer(pattern, content)
    
    total = 0
    enabled = True  
    
    for match in matches:
        instruction = match.group(0)
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                x, y = map(int, match.groups())
                result = x * y
                total += result
    
    return total

if __name__ == "__main__":
    result = solve_mul_instructions("mul.txt")
    print(f"The sum of all multiplication results is: {result}")

