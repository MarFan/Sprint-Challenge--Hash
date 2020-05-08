def has_negatives(a):

    """
    YOUR CODE HERE
    """
    result = []
    num_hash = {}

    # print(a)

    for num in a:
    	fixed_num = abs(num)

    	if fixed_num not in num_hash:
    		num_hash[fixed_num] = 0
    	elif fixed_num in num_hash:
    		num_hash[fixed_num] += 1

    	if num_hash[fixed_num] > 0:
    		result.append(fixed_num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
