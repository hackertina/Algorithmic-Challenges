from DataStructures.LinkedLists.linked_list_utils import array_to_linked_list, linked_list_to_array

from DataStructures.LinkedLists.merge_two_sorted_lists import Solution


def test_merge_two_lists():
    list1 = array_to_linked_list([1,2,4])
    list2 = array_to_linked_list([1,3,4])
    solution = Solution()
    result_head = solution.mergeTwoLists(list1, list2)
    result_array = linked_list_to_array(result_head)
    assert result_array == [1,1,2,3,4,4], f"Expected [1,1,2,3,4,4], got {result_array}"

# Optionally, you can call the test function here or use a test runner/framework
if __name__ == "__main__":
    test_merge_two_lists()
    print("Test passed.")
