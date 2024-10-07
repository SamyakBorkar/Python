def ss_sl(L):
    def make_list(L):
        temp_list = []

        for item in L:
            if isinstance(item, (int, float)):
                temp_list.append(item)
            elif isinstance(item, (list, tuple, set)):
                temp_list.extend(make_list(item))
            elif isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(key, (int, float)):
                        temp_list.append(key)
                    if isinstance(value, (int, float)):
                        temp_list.append(value)
                    elif isinstance(value, (list, tuple, set)):
                        temp_list.extend(make_list(value))

        return temp_list

    temp_numbers = make_list(L)

    if len(temp_numbers) == 0:
        return "No valid numbers found in the structure"
    if len(temp_numbers) == 1:
        return temp_numbers[0], "Only one distinct number found"

    temp_numbers = sorted(set(temp_numbers))


    second_smallest = None
    for i in range(1, len(temp_numbers)):
        if temp_numbers[i] != temp_numbers[0]:
            second_smallest = temp_numbers[i]
            break


    second_largest = None
    for i in range(len(temp_numbers) - 2, -1, -1):
        if temp_numbers[i] != temp_numbers[-1]:
            second_largest = temp_numbers[i]
            break

    return second_smallest, second_largest


Dummy_List = [1, [22.7, 3, 4], 5, 5.5, {5: 6, 7: 8}, (10, 2), {"key": 9}, {3: 4, 5: 6}]
second_smallest, second_largest = ss_sl(Dummy_List)
print(f"Second Smallest: {second_smallest}, Second Largest: {second_largest}")
