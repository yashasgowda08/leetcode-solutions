class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            reserved.setdefault(row, set()).add(seat)

        # Initially every row can fit 2 families
        ans = 2 * n

        for seats in reserved.values():
            left = {2, 3, 4, 5}
            right = {6, 7, 8, 9}
            middle = {4, 5, 6, 7}

            can_left = not (seats & left)
            can_right = not (seats & right)
            can_middle = not (seats & middle)

            if can_left and can_right:
                # Both groups fit
                continue
            elif can_left or can_right or can_middle:
                # Only one group fits
                ans -= 1
            else:
                # No group fits
                ans -= 2

        return ans