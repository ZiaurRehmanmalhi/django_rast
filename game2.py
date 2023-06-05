# def reverse(string):
#     return string[::-1]
#
#
# def is_palandrom(string):
#     return string == reverse(string)
#
#
# print(is_palandrom("civic"))


# def dictionary_creator(list1, list2):
#     # this line ensures both lists are of same size/length
#     assert len(list1) == len(list2)
#
#     dictionary = {}
#     for i in range(len(list1)):
#         dictionary[list1[i]] = list2[i]
#
#     return dictionary
#
#
# dictionary_creator(["a", "b", "c"], [1, 2, 3])  # => {"a":1, "b":2, "c":3}
# dictionary_creator(
#     ["shirts", "abaya", "diapers"], ["men", "women", "kids"]
# )

def running_sum(arr):
    running_total = 0
    result = []

    for num in arr:
        running_total += num
        result.append(running_total)

    return result


# Example usage
my_array = [1, 2, 3, 4, 5]
result_array = running_sum(my_array)

print(result_array)

