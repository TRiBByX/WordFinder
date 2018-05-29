def createList(length):
    nums = []
    for x in range(0, length):
        if x is not 65:
            nums.append(x)
    return nums


def binarySearch(num, nums):
    u_lim = int(len(nums))
    l_lim = int(0)
    print 'Doing binary search...'

    while l_lim <= u_lim:
        i = (l_lim + u_lim) // 2
        print nums[64]
        print i, nums[i]
        if nums[i] == num:
            return '{num} found at index {i}'.format(num=num, i=i)
        elif nums[i] > num:
            u_lim = i - 1
        elif nums[i] < num:
            l_lim = i + 1
        else:
            return '{num} not found in list'.format(num=num)

if __name__ == "__main__":
    nums = createList(100)
    print binarySearch(65, nums)
