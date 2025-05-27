# Test Cases for Eliminator 1: Student Grade Aggregation

def test_eliminator_1():
    """Comprehensive test cases for get_top_students function"""
    
    # Test Case 1: Basic functionality
    test_scores_1 = [
        {"name": "Alice", "test": "Math", "score": 85},
        {"name": "Bob", "test": "Math", "score": 90},
        {"name": "Alice", "test": "Science", "score": 95},
        {"name": "Charlie", "test": "Math", "score": 78}
    ]
    expected_1 = [
        {"name": "Alice", "average": 90.0},
        {"name": "Bob", "average": 90.0},
        {"name": "Charlie", "average": 78.0}
    ]
    result_1 = get_top_students(test_scores_1, 3)
    print("Test 1 - Basic:", result_1 == expected_1)
    
    # Test Case 2: Tie breaking (same average, alphabetical order)
    test_scores_2 = [
        {"name": "Zoe", "test": "Math", "score": 85},
        {"name": "Alice", "test": "Math", "score": 85},
        {"name": "Bob", "test": "Math", "score": 90}
    ]
    expected_2 = [
        {"name": "Bob", "average": 90.0},
        {"name": "Alice", "average": 85.0},
        {"name": "Zoe", "average": 85.0}
    ]
    result_2 = get_top_students(test_scores_2, 3)
    print("Test 2 - Tie Breaking:", result_2 == expected_2)
    
    # Test Case 3: Limiting results
    test_scores_3 = [
        {"name": "Alice", "test": "Math", "score": 95},
        {"name": "Bob", "test": "Math", "score": 85},
        {"name": "Charlie", "test": "Math", "score": 75},
        {"name": "Diana", "test": "Math", "score": 65}
    ]
    expected_3 = [
        {"name": "Alice", "average": 95.0},
        {"name": "Bob", "average": 85.0}
    ]
    result_3 = get_top_students(test_scores_3, 2)
    print("Test 3 - Limiting:", result_3 == expected_3)
    
    # Test Case 4: Multiple tests per student with decimal averages
    test_scores_4 = [
        {"name": "Alice", "test": "Math", "score": 90},
        {"name": "Alice", "test": "Science", "score": 85},
        {"name": "Alice", "test": "History", "score": 92},
        {"name": "Bob", "test": "Math", "score": 88},
        {"name": "Bob", "test": "Science", "score": 90}
    ]
    expected_4 = [
        {"name": "Bob", "average": 89.0},
        {"name": "Alice", "average": 89.0}
    ]
    result_4 = get_top_students(test_scores_4, 2)
    print("Test 4 - Multiple Tests:", result_4 == expected_4)
    
    # Test Case 5: Edge case - empty input
    test_scores_5 = []
    expected_5 = []
    result_5 = get_top_students(test_scores_5, 3)
    print("Test 5 - Empty Input:", result_5 == expected_5)
    
    # Test Case 6: Edge case - zero students requested
    test_scores_6 = [{"name": "Alice", "test": "Math", "score": 85}]
    expected_6 = []
    result_6 = get_top_students(test_scores_6, 0)
    print("Test 6 - Zero Students:", result_6 == expected_6)
    
    # Test Case 7: Edge case - more students requested than available
    test_scores_7 = [
        {"name": "Alice", "test": "Math", "score": 85},
        {"name": "Bob", "test": "Math", "score": 90}
    ]
    expected_7 = [
        {"name": "Bob", "average": 90.0},
        {"name": "Alice", "average": 85.0}
    ]
    result_7 = get_top_students(test_scores_7, 5)
    print("Test 7 - More Requested:", result_7 == expected_7)
    
    # Test Case 8: Edge case - perfect and zero scores
    test_scores_8 = [
        {"name": "Perfect", "test": "Math", "score": 100},
        {"name": "Zero", "test": "Math", "score": 0},
        {"name": "Average", "test": "Math", "score": 50}
    ]
    expected_8 = [
        {"name": "Perfect", "average": 100.0},
        {"name": "Average", "average": 50.0},
        {"name": "Zero", "average": 0.0}
    ]
    result_8 = get_top_students(test_scores_8, 3)
    print("Test 8 - Extreme Scores:", result_8 == expected_8)
    
    # Test Case 9: Edge case - invalid/missing data
    test_scores_9 = [
        {"name": "Alice", "test": "Math", "score": 85},
        {"name": "Bob", "test": "Math"},  # Missing score
        {"test": "Math", "score": 90},   # Missing name
        {"name": "Charlie", "test": "Math", "score": "invalid"},  # Invalid score
        {"name": "Diana", "test": "Math", "score": -10},  # Negative score
        {"name": "Eve", "test": "Math", "score": 110}     # Score > 100
    ]
    expected_9 = [
        {"name": "Alice", "average": 85.0},
        {"name": "Bob", "average": 0.0},
        {"name": "Charlie", "average": 0.0},
        {"name": "Diana", "average": 0.0},
        {"name": "Eve", "average": 0.0}
    ]
    result_9 = get_top_students(test_scores_9, 5)
    print("Test 9 - Invalid Data:", result_9 == expected_9)
    
    # Test Case 10: Complex scenario with decimal rounding
    test_scores_10 = [
        {"name": "Alice", "test": "Test1", "score": 83},
        {"name": "Alice", "test": "Test2", "score": 87},
        {"name": "Alice", "test": "Test3", "score": 85},  # Average: 85.0
        {"name": "Bob", "test": "Test1", "score": 84},
        {"name": "Bob", "test": "Test2", "score": 86},    # Average: 85.0 (tie)
        {"name": "Charlie", "test": "Test1", "score": 90},
        {"name": "Charlie", "test": "Test2", "score": 88},
        {"name": "Charlie", "test": "Test3", "score": 89}, # Average: 89.0
    ]
    expected_10 = [
        {"name": "Charlie", "average": 89.0},
        {"name": "Alice", "average": 85.0},  # Alphabetically before Bob
        {"name": "Bob", "average": 85.0}
    ]
    result_10 = get_top_students(test_scores_10, 3)
    print("Test 10 - Complex Tie:", result_10 == expected_10)
    
    # Test Case 11: Single student, multiple tests
    test_scores_11 = [
        {"name": "Solo", "test": "Math", "score": 90},
        {"name": "Solo", "test": "Science", "score": 85},
        {"name": "Solo", "test": "History", "score": 95},
        {"name": "Solo", "test": "English", "score": 88}
    ]
    expected_11 = [
        {"name": "Solo", "average": 89.5}
    ]
    result_11 = get_top_students(test_scores_11, 1)
    print("Test 11 - Single Student:", result_11 == expected_11)
    
    # Test Case 12: Negative num_students
    test_scores_12 = [{"name": "Alice", "test": "Math", "score": 85}]
    expected_12 = []
    result_12 = get_top_students(test_scores_12, -1)
    print("Test 12 - Negative Request:", result_12 == expected_12)

# Expected behavior summary:
"""
Pass Criteria:
- Handles all basic cases correctly (Tests 1-4)
- Proper edge case handling (Tests 5-7)
- Correct data validation (Tests 8-9)
- Accurate tie-breaking and rounding (Tests 10-11)
- Graceful error handling (Test 12)

The function should pass ALL tests to demonstrate competency.
"""