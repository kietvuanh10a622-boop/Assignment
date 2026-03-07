def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    result_list = remove_odds(test_list)
    
    print(f"Original list: {test_list}")
    print(f"Cut-down list: {result_list}")