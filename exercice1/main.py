# nums[i] + nums[j] = target

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_dict(nums, target):
    seen_num = {}

    for i, num in enumerate(nums):
        reste = target - num
        if reste in seen_num:
            return [seen_num[reste], i]
        seen_num[num] = i
    return []    

def exec_fcnt():
    # Saisir nums :
    nums_input = input("Entrer des nombres séparés par espace : ")

    liste_nums_str = nums_input.split()
    nums = []

    for x in liste_nums_str:
        nums.append(int(x))

    print(nums)

    # Saisir target :
    target_input = input("Saisir la valeur de target : ")

    target = int(target_input)

    return two_sum_dict(nums, target)

print(exec_fcnt())