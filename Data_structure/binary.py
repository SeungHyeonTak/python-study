#Binary Search :이진탐색_알고리즘
#최악의 경우

def binary(target, data):
    data.sort() #내림차순정렬
    start = 0
    end = len(data) - 1 #마지막꺼 제외?
    while start <= end: # 시작보다 마지막이 작아야지 정렬을 했는데
        mid = (start + end) // 2 # 중간index를 구한다

        if data[mid] == target: # 찾는값이랑 target이랑 같을때
            return mid # 그 값 출력
        elif data[mid] < target: # 찾는값보다 target이 더 클때
            start = mid + 1 # 중간값을 1추가하여 시작을 다시 한다
        else:
            end = mid - 1 # 찾는값이 작으면 mid를 하나씩 낮추면서 찾는다

    return None

if __name__ == "__main__":
    target = 19
    #li = [i**2 for i in range(11)]
    li = [i for i in range(1,20)]
    arr = binary(target,li)

    if arr:
        print(li)
        print(li[arr])
    else:
        print(f"찾으시는 타겟 {target}가 없습니다.")
