from search import verify_query


def test_verify_query():
    # Test case 1: Empty query
    assert verify_query("") is False

    # Test case 2: Query with length 1
    assert verify_query("a") is False

    # Test case 3: Valid query returns a non-empty list
    assert verify_query("apple") is not False

    # Test case 4: Query with leading/trailing spaces
    assert verify_query("  apple  ") is not False

    # Test case 5: Query with special characters
    assert len(verify_query("apple!")) > 0

    # Test case 6: Query with numbers
    assert verify_query("apple123") is not False

    # Test case 7: Query with valid length
    assert (
        len(verify_query("apple pie")) > 0
    )  # Assuming search() returns a non-empty list

    print("All test cases passed!")


test_verify_query()
