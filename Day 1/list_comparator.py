# Calculating total distance
def calculate_total_distance(left, right):
    # Sort both lists and find the distance
    leftlist = sorted(left)
    rightlist = sorted(right)
    total = 0
    for l, r in zip(leftlist, rightlist): # zip combines into pairs for easy access
        total += abs(l - r) 
    return total

# Calculating similarity
def calculate_similarity_score(left, right):
    # Count how many times each number appears in the right list (key: value for each number where value is number of appearances)
    right_counts = {}
    for number in right:
        if number in right_counts:
            right_counts[number] += 1
        else:
            right_counts[number] = 1

    # Calculate similarity score
    total = 0
    for number in left:
        total += number * right_counts.get(number, 0)  
    return total

# Read input from file
def read_file(file_path):
    left = []
    right = []
    with open(file_path, 'r') as file:
        for line in file:
            l, r = map(int, line.split())  # split into right and left list
            left.append(l)
            right.append(r)
    return left, right

def main(file_path):
    left, right = read_file(file_path)  
    distance = calculate_total_distance(left, right)  
    print("Total Distance:", distance)
    similarity = calculate_similarity_score(left, right)  
    print("Similarity Score:", similarity)


file_path = "input.txt" 
main(file_path)
