
# P1
# if __name__ == "__main__":
#     file = open("input.txt")
#     lines: list[str] = file.read().splitlines()

#     total: int = 0

#     for line in lines:
#         curr: str = ""
#         for char in line:
#             if char.isdigit():
#                 curr += char

#         total += int(curr[0] + curr[-1])

#     print(total)

# P2
if __name__ == "__main__":
    file = open("input.txt")
    lines: list[str] = file.read().splitlines()
    file.close()

    total: int = 0

    nums: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    total: int = 0
    # The longest named number is only 5 chars, so no need to check farther than that
    MAX_STR_LENGTH: int = 5

    # Idea: Loop over chars of each line
    #       If the char is a digit, add to vals
    #       Otherwise, add char to possible_num to keep track of named number building
    #       Check if possible_num is a named num, and if so, add to vals
    #       If len(possible_num) is ever MAX_STR_LENGTH and not a named number, reset pos back

    for line in lines:
        pos: int = 0            # Position in the line
        possible_num: str = ""  # Keep track of named numbers
        vals: list = []         # Keep track of found numbers in the line

        while pos < len(line):
            curr: str = line[pos]

            if curr.isdigit():
                # Can still have a number hidden in the current possible_num
                while possible_num:
                    if possible_num in nums:
                        vals.append(nums[possible_num])

                    possible_num = possible_num[1:]

                vals.append(int(curr))

                pos += 1
                continue

            possible_num += curr

            # The current possible num is a named number
            if possible_num in nums:
                vals.append(nums[possible_num])
                possible_num = ""

                # We add back the current char because can have a situation like 'oneight'
                # where we have both 1 and 8 sharing a letter
                possible_num += curr

            # We have reached the max named number length with no found number
            if len(possible_num) == MAX_STR_LENGTH:
                possible_num = ""
                pos -= (MAX_STR_LENGTH - 1)

            pos += 1

        # Can still have a number hidden in possible_num at the end, so check for that
        while possible_num:
            if possible_num in nums:
                vals.append(nums[possible_num])

            possible_num = possible_num[1:]

        total += ((vals[0] * 10) + vals[-1])

    print(total)
