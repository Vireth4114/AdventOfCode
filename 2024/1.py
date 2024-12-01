import useful

lines = [useful.get_numbers(line) for line in useful.get_lines("1")]
nums1, nums2 = zip(*lines)

def silverstar():
    print(sum(abs(i[0] - i[1]) for i in zip(sorted(nums1), sorted(nums2))))

def goldstar():
    print(sum(i*nums2.count(i) for i in nums1))

if __name__ == "__main__":
    silverstar()
    goldstar()

