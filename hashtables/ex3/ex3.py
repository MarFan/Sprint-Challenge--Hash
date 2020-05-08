def intersection(arrays):

    """
    YOUR CODE HERE
    """
    ugly_hash = {}
    result = []

    # not what I want...
    # there's got to be a better way...
    for i in arrays:
    	for num in i:
            if num in ugly_hash:
                ugly_hash[num] += 1
            elif num not in ugly_hash:
                ugly_hash[num] = 1

            if ugly_hash[num] == len(arrays):
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
