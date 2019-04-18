# 이진탐색_Binary search
# 알고리즘
# 재귀함수로 풀이
# *반드시 정렬된 상태에서 시작해야한다.

def binary(target, start, end, li_data):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if li_data[mid] == target:
        return mid
    elif li_data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return binary(target , start, end, li_data)

if __name__ == "__main__":
    tg = int(input("taget으로 정할 수를 입력하시오 : "))
    li = [i for i in range(0,20)]
    
    # taget ,start, end, li를 함수의 파라미터로 주자
    index = binary(tg, 0, len(li), li)
    print(li)
    print(index)
