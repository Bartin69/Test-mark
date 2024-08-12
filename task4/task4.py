def min_moves_to_equal_elements(nums):

    nums.sort()
    median = nums[len(nums) // 2]


    moves = sum(abs(num - median) for num in nums)

    return moves

def main():

    file_path = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task4\numbers.txt'

    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]

    result = min_moves_to_equal_elements(nums)

    print(result)

if __name__ == "__main__":
    main()
