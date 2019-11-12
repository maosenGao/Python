# -*- coding: utf-8 -*-

"""
	In this problem, we want to determine all possible combinations of k
	numbers out of 1 ... n. We use backtracking to solve this problem.


	Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!)))

    在这个问题中，我们想要确定所有k个数字的可能组合。
    我们用回溯法来解决这个问题。
    
    时间复杂度:o(c(n,k))即o(n选k) =o((n!/(k!)* (n - k) !)))
"""


def generate_all_combinations(n: int, k: int) -> [[int]]:
    """
    >>> generate_all_combinations(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    
    result = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(increment, total_number, level, current_list, total_list):
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


def print_all_state(total_list):
    for i in total_list:
        print(*i)


if __name__ == '__main__':
    n = 4
    k = 2
    total_list = generate_all_combinations(n, k)
    print_all_state(total_list)
