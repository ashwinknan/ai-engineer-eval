# Test Cases for Eliminator 2: Text Analysis with Filtering

def test_eliminator_2():
    """Comprehensive test cases for analyze_text function"""
    
    # Test Case 1: Basic functionality
    text_1 = "The quick brown fox jumps over the lazy dog. The fox was quick!"
    expected_1 = {"quick": 2, "fox": 2}
    result_1 = analyze_text(text_1, 2)
    print("Test 1 - Basic:", result_1 == expected_1)
    
    # Test Case 2: Punctuation removal
    text_2 = "Hello, world! Hello? World... hello-world hello@world hello/world."
    expected_2 = {"hello": 4, "world": 4}
    result_2 = analyze_text(text_2, 2)
    print("Test 2 - Punctuation:", result_2 == expected_2)
    
    # Test Case 3: Case normalization
    text_3 = "Test TEST tEsT test Test"
    expected_3 = {"test": 5}
    result_3 = analyze_text(text_3, 3)
    print("Test 3 - Case:", result_3 == expected_3)
    
    # Test Case 4: Common word filtering
    text_4 = "The cat and dog are in the house with the owner"
    expected_4 = {}  # All words are either common words or appear only once
    result_4 = analyze_text(text_4, 2)
    print("Test 4 - Common Words:", result_4 == expected_4)
    
    # Test Case 5: Contractions
    text_5 = "Don't worry, we'll handle it's processing. Don't stress."
    expected_5 = {"do": 2, "not": 2, "worry": 1, "will": 1, "handle": 1, "processing": 1, "stress": 1}
    result_5 = analyze_text(text_5, 1)
    print("Test 5 - Contractions:", result_5 == expected_5)
    
    # Test Case 6: Minimum frequency threshold
    text_6 = "apple banana apple cherry apple banana"
    expected_6 = {"apple": 3}
    result_6 = analyze_text(text_6, 3)
    print("Test 6 - Frequency Threshold:", result_6 == expected_6)
    
    # Test Case 7: Edge case - empty text
    text_7 = ""
    expected_7 = {}
    result_7 = analyze_text(text_7, 1)
    print("Test 7 - Empty Text:", result_7 == expected_7)
    
    # Test Case 8: Edge case - None input
    text_8 = None
    expected_8 = {}
    result_8 = analyze_text(text_8, 1)
    print("Test 8 - None Text:", result_8 == expected_8)
    
    # Test Case 9: Edge case - zero/negative min_frequency
    text_9 = "hello world hello"
    expected_9 = {"hello": 2, "world": 1}
    result_9 = analyze_text(text_9, 0)  # Should treat as min_frequency = 1
    print("Test 9 - Zero Frequency:", result_9 == expected_9)
    
    # Test Case 10: Minimum word length (2+ characters)
    text_10 = "I am a big fan of AI and ML in CS"
    expected_10 = {"am": 1, "big": 1, "fan": 1, "ai": 1, "ml": 1, "cs": 1}
    result_10 = analyze_text(text_10, 1)
    print("Test 10 - Min Length:", result_10 == expected_10)
    
    # Test Case 11: Complex contractions
    text_11 = "I'm sure you're right, they're coming, we're ready"
    # Should expand to: "I am sure you are right they are coming we are ready"
    expected_11 = {"sure": 1, "right": 1, "coming": 1, "ready": 1}
    result_11 = analyze_text(text_11, 1)
    print("Test 11 - Complex Contractions:", result_11 == expected_11)
    
    # Test Case 12: Special characters and numbers
    text_12 = "test123 test@#$% test_test test-case test test"
    expected_12 = {"test": 4, "testtest": 1, "testcase": 1}
    result_12 = analyze_text(text_12, 1)
    print("Test 12 - Special Chars:", result_12 == expected_12)
    
    # Test Case 13: Mixed frequency requirements
    text_13 = "apple apple banana banana cherry date date date"
    expected_13 = {"date": 3}  # Only date appears 3+ times
    result_13 = analyze_text(text_13, 3)
    print("Test 13 - Mixed Frequency:", result_13 == expected_13)
    
    # Test Case 14: Only punctuation and common words
    text_14 = "The, and! but? or... if; when: because."
    expected_14 = {}
    result_14 = analyze_text(text_14, 1)
    print("Test 14 - Only Common/Punct:", result_14 == expected_14)
    
    # Test Case 15: Unicode and special characters
    text_15 = "café café naïve naïve résumé résumé"
    expected_15 = {"café": 2, "naïve": 2, "résumé": 2}
    result_15 = analyze_text(text_15, 2)
    print("Test 15 - Unicode:", result_15 == expected_15)
    
    # Test Case 16: Long text with various patterns
    text_16 = """
    The quick brown fox jumps over the lazy dog. The dog was lazy, 
    and the fox was quick. Quick movements and lazy afternoons - 
    that's life for a fox and dog. The fox found peace, while the 
    dog found comfort. Both the quick fox and lazy dog were happy.
    """
    expected_16 = {"fox": 5, "quick": 4, "lazy": 4, "dog": 4, "found": 2}
    result_16 = analyze_text(text_16, 2)
    print("Test 16 - Long Text:", result_16 == expected_16)
    
    # Test Case 17: Contractions with punctuation
    text_17 = "Don't! Can't? Won't... shouldn't, wouldn't."
    # Should expand and clean properly
    expected_17 = {"do": 1, "not": 1, "can": 1, "will": 1, "should": 2, "would": 1}
    result_17 = analyze_text(text_17, 1)
    print("Test 17 - Contractions + Punct:", result_17 == expected_17)
    
    # Test Case 18: Edge case - single character words
    text_18 = "A B C a b c I a I"
    expected_18 = {}  # All single characters or common words should be filtered
    result_18 = analyze_text(text_18, 1)
    print("Test 18 - Single Chars:", result_18 == expected_18)

# Standard contractions that should be handled:
CONTRACTIONS_REFERENCE = {
    "don't": "do not",
    "won't": "will not", 
    "can't": "cannot",
    "shouldn't": "should not",
    "wouldn't": "would not",
    "couldn't": "could not",
    "mustn't": "must not",
    "needn't": "need not",
    "i'm": "i am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is", 
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",
    "i've": "i have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "i'll": "i will",
    "you'll": "you will",
    "he'll": "he will",
    "she'll": "she will",
    "we'll": "we will",
    "they'll": "they will",
    "i'd": "i would",
    "you'd": "you would",
    "he'd": "he would",
    "she'd": "she would",
    "we'd": "we would",
    "they'd": "they would"
}

# Common words to exclude (case-insensitive):
COMMON_WORDS = {
    'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
    'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 
    'do', 'does', 'did', 'will', 'would', 'could', 'should', 'can', 'may', 
    'might', 'must', 'shall', 'this', 'that', 'these', 'those',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
    'my', 'your', 'his', 'its', 'our', 'their'
}

"""
Pass Criteria:
- Correctly processes all text normalization (Tests 1-3)
- Proper filtering of common words (Test 4)
- Accurate contraction handling (Tests 5, 11, 17)
- Correct frequency thresholding (Tests 6, 13)
- Graceful edge case handling (Tests 7-9)
- Proper minimum word length filtering (Test 10)
- Handles special characters and unicode (Tests 12, 15)
- Works with longer, realistic text (Test 16)

The function should pass ALL tests to demonstrate competency.
"""