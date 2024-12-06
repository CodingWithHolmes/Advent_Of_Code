def read_word_search(filename):
    try:
        with open(filename) as f:
            lines = [line.strip() for line in f]
            if not lines:
                raise ValueError("File is empty")
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {filename}")

def count_xmas_part1(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def check_direction(row, col, dx, dy):
        if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
            return False
        word = ''
        for i in range(4): 
            word += grid[row + i*dx][col + i*dy]
        return word == 'XMAS'
    
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    count += 1
    
    return count

def count_xmas_part2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_x_pattern(row, col):
        if not (0 <= row - 1 < rows and 0 <= row + 1 < rows and 
                0 <= col - 1 < cols and 0 <= col + 1 < cols):
            return False
            
        top_left = grid[row-1][col-1]
        top_right = grid[row-1][col+1]
        center = grid[row][col]
        bottom_left = grid[row+1][col-1]
        bottom_right = grid[row+1][col+1]
        
        valid_patterns = [
            (top_left + center + bottom_right == "MAS" and top_right + center + bottom_left == "MAS"),
            (top_left + center + bottom_right == "MAS" and top_right + center + bottom_left == "SAM"),
            (top_left + center + bottom_right == "SAM" and top_right + center + bottom_left == "MAS"),
            (top_left + center + bottom_right == "SAM" and top_right + center + bottom_left == "SAM")
        ]
        
        return any(valid_patterns)
    
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if check_x_pattern(row, col):
                count += 1
    
    return count

def main():
    try:
        grid = read_word_search('wordsearch.txt')
        
        result1 = count_xmas_part1(grid)
        print(f"Part 1: XMAS appears {result1} times in the word search")
        
        result2 = count_xmas_part2(grid)
        print(f"Part 2: X-MAS appears {result2} times in the word search")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure 'wordsearch.txt' exists in the same directory as this script and contains the word search puzzle.")

if __name__ == "__main__":
    main()
