# calculates the different permutations of 2x1 and 3x1 floor tiles in a width
def generate_permutations(row, remaining_width):
    if remaining_width == 0:
        return [row] 

    master_list = []

    # 2x1
    if remaining_width >= 2:
        master_list.extend(generate_permutations(row + [2], remaining_width - 2))

    # 3x1
    if remaining_width >= 3:
        master_list.extend(generate_permutations(row + [3], remaining_width - 3))

    return master_list

# calculates conflict matrix between different permutations
def generate_conflict_matrix(floor_permutations, w):
    num_permutations = len(floor_permutations)
    
    floor_sets = [generate_set(floor, w) for floor in floor_permutations]

    # checks if there is overlap in the sets
    conflict_matrix = [[] for i in range(len(floor_permutations))]
    for i in range(num_permutations):
        for j in range(num_permutations):
            if (floor_sets[i].isdisjoint(floor_sets[j])):
                conflict_matrix[i].append(j)

    return conflict_matrix

# helper for generate_conflict_matrix; generates sets from permutations
def generate_set(floor_permutation, w):
    location = 0
    permutation_set = set()

    for floorboard in floor_permutation:
        location += floorboard
        permutation_set.add(location)

    permutation_set.remove(w)
    return permutation_set

# solves the floor problem
def floor_problem(w, h): 
    # initialization
    permutations = generate_permutations([], w)
    num_permutations = len(permutations)
    conflict_matrix = generate_conflict_matrix(permutations, w)

    # uses dp & shallow copy to find the amount of floors possible
    dp_floors = num_permutations * [1]
    temp_count = 0
    for i in range(1, h):
        temp_dp_floors = dp_floors.copy()
        for j in range(num_permutations):
            for k in conflict_matrix[j]:
                temp_count += temp_dp_floors[k]
            
            dp_floors[j] = temp_count
            temp_count = 0

    return sum(dp_floors)

print(floor_problem(9, 3)) #8
print(floor_problem(32, 10)) #806844323190414
