def read_input():
    file_path = input()
    nums = []
    with open(file_path, 'r') as file:
        for line in file:
            nums.append(int(line.strip()))
    nums.sort()
    return nums

def find_deviations_sum(nums):
    median_index = len(nums) // 2
    sum = 0
    for num in nums:
        sum += abs(num - nums[median_index])
    return sum

if __name__ == '__main__':
    nums = read_input()
    print(find_deviations_sum(nums))
