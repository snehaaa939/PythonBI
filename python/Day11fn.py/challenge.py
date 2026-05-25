# You have a numbers stored in a list as [1, -3, 0, 2, 0, 7, 10, 8, -1].
# Write a function get_data(l, r, x) that find the sum of number from position l to r.
# If 0 lies in that given range it has to be replaced by value x.


# Example: if l = 2, r = 6 and x = 5 then sum of item from position 2 to 6 is 19. Since there are two zeros replacing it by 5 gives: 19 + 5 + 5 i.e. 29 as output.
def get_data(l, r, x):
    num_list = [1, -3, 0, 2, 0, 7, 10, 8, -1]
    sub_list = num_list[l : r + 1]
    count_zero = sub_list.count(0)
    sum_list = sum(sub_list)
    sum_list = sum_list + count_zero * x
    return sum_list


result = get_data(2, 6, 5)
print(result)
