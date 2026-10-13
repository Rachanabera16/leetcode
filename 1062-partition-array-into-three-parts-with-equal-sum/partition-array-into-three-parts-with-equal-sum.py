

class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        current_sum = 0
        parts = 0

        for num in arr:
            current_sum += num

            if current_sum == target:
                parts += 1
                current_sum = 0

                if parts == 3:
                    return True

        return False
