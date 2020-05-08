def finder(files, queries):

    """
    YOUR CODE HERE
    """
    result = []
    #file_hash = {}
    query_hash = {}

    for query in queries:
        if query not in query_hash:
            query_hash[query] = query

    for file in files:
        file_name = file.split('/')[-1]
        if file_name in query_hash:
            result.append(file)

    # only shows the file once if storing the filename in a hashtable
    # for file in files:
    #     file_name = file.split('/')[-1]
    #     print(file_name)
    #     if file_name not in file_hash:   
    #         file_hash[file_name] = file

    # for query in queries:
    #     if query in file_hash:
    #         result.append(file_hash[query])

    # print(file_hash.items())

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
