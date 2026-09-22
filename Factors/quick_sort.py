nums = [3, 1, 2, 4, 6, 7, 8]

def qick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)

        qick_sort(nums, low, p_ind - 1)
        qick_sort(nums, p_ind + 1, high)


def partition(nums, low, high):
    pivot = nums[low]

    i = low
    j = high

    while i < j:

        while nums[i] <= pivot and i <= high - 1:
            i += 1

        while nums[j] > pivot and j > low:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j


qick_sort(nums, 0, len(nums) - 1)

print(nums)