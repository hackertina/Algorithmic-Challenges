from DataStructures.LinkedLists.linked_list_utils import array_to_linked_list, linked_list_to_array

from DataStructures.LinkedLists.remove_duplicates_from_sorted_list import Solution


def test_remove_duplicates_from_sorted_list():
    head = array_to_linked_list([1,1,2,3,3])
    solution = Solution()
    result_head = solution.deleteDuplicates(head)
    result_array = linked_list_to_array(result_head)
    assert result_array == [1,2,3], f"Expected [1,2,3], got {result_array}"

# Optionally, you can call the test function here or use a test runner/framework
if __name__ == "__main__":
    test_remove_duplicates_from_sorted_list()
    print("Test passed.")
