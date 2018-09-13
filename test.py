def turn_zero(value, turn_zero_list, picture):
    if len(turn_zero_list) == 0:
        return num_of_this_value

    for index_y, index_x in turn_zero_list:

        picture[index_y][index_x] = 0

        turn_zero_list.pop(0)

        if (index_x + 1) <= (n - 1):
            right = picture[index_y][index_x + 1]
            if right == value:
                turn_zero_list.append((index_y, index_x + 1))
                num_of_this_value += 1

        if (index_x - 1) >= 0:
            left = picture[index_y][index_x - 1]
            if left == value:
                turn_zero_list.append((index_y, index_x - 1))
                num_of_this_value += 1

        if (index_y + 1) <= (m - 1):
            bottom = picture[index_y + 1][index_x]
            if bottom == value:
                turn_zero_list.append((index_y + 1, index_x))
                num_of_this_value += 1

        turn_zero(value, turn_zero_list, picture, num_of_this_value)


def solution(m, n, picture):
    result_list = []
    for index_y in range(0, m):
        for index_x in range(0, n):

            #             print('@@@@@@@@')
            #             print(index_y)
            #             print(index_x)

            value = picture[index_y][index_x]

            print('@@@@@@@@@')
            if value == 0:
                continue

            turn_zero_list = []

            # 기준좌표를 저장,
            turn_zero_list.append((index_y, index_x))
            num_of_this_value = 1

            turn_zero(value, turn_zero_list, picture, num_of_this_value)

            #             # 1차적으로 기준좌표에서 접근가능한 3방향 중 기준 좌표와 value 같으면 그 좌표 저장.
            #             if (index_x+1) <= (n-1):
            #                 right = picture[index_y][index_x+1]
            #                 if right == value:
            #                     turn_zero_list.append((index_y,index_x+1))

            #             if (index_x-1)>=0:
            #                 left = picture[index_y][index_x-1]
            #                 if left == value:
            #                     turn_zero_list.append((index_y, index_x-1))

            #             if (index_y+1)<=(m-1):
            #                 bottom = picture[index_y+1][index_x]
            #                 if bottom == value:
            #                     turn_zero_list.append((index_y+1, index_x))

            result_list.append((value, len(turn_zero_list))  # 색상값, 그수 튜플로 리스트에 추가.

    return result_list

