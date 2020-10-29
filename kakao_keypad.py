def solution(numbers, hand):
    answer = ''
    # 리스트로 0~9 까지 키패드 좌표 만들어줌(거리 구하기 위해). 리스트로 만들어서 선택하기 쉽게
    keypad = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1]]
    
    # 초기 위치 좌표
    left = [0, 0]
    right = [2, 0]
    
    left_side = [1, 4, 7]
    right_side = [3, 6, 9]
    
    # 입력된 숫자들 체크
    for num in numbers :
         # 바뀌는 키패드 좌표
        key = keypad[num]
        
        if num in left_side :
            answer += 'L'
            left = key
        elif num in right_side :
            answer += 'R'
            right = key
        else :
            # 키패드 중간에 있는 숫자들 판별 방법 : 왼쪽과 num, 오른쪽과 num 의 위치를 계산해서 'L'인지'R'인지 선택
            x, y = key
            dist_l = abs(x - left[0]) + abs(y - left[1])
            dist_r = abs(x - right[0]) + abs(y - right[1])

            if dist_l < dist_r :
                answer += 'L'
                left = key
            elif dist_l > dist_r :
                answer += 'R'
                right = key
            # 숫자가 같으면 왼손잡인지 오른손잡인지 인자로 구분
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = key
                elif hand == 'left' :
                    answer += 'L'
                    left = key

    return answer