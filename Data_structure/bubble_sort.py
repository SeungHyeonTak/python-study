# 버블정렬_bubble sort
# 인접한 두 원소를 검사하여 정렬하는 방법

def bubble(li):
    for i in range(len(li) - 1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
if __name__ == "__main__":
    li = [6,5,3,4]
    print(bubble(li))
