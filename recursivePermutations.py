# Recursively Print all Permutations of a String
def permutations(word):

    # Base case: Empty string
    if len(word) == 0:
        return []

    # Base case: Single character
    elif len(word) == 1:
        return [word]

    # Recursive case: Find all permutations of first character
    # of word with all permutations of remaining substring
    else:
        perms = []
        for i in permutations(word[1:]):
            for j in range(len(word)):
                perms.append(i[:j] + word[0] + i[j:])
    return perms


# Print out results
for permutation in permutations('ALEX'):
    print(permutation)
