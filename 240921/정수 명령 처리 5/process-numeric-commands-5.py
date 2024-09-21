# 동적 배열을 위한 리스트 초기화
arr = []

# 명령의 개수 입력
n = int(input())

# 명령어를 처리하는 루프
for _ in range(n):
    command = input().split()  # 명령어를 공백으로 구분하여 입력 받음

    if command[0] == "push_back":
        # push_back 명령일 때, 두 번째 인자가 배열에 추가됨
        arr.append(int(command[1]))
    elif command[0] == "pop_back":
        # pop_back 명령일 때, 배열의 마지막 요소 제거
        arr.pop()
    elif command[0] == "size":
        # size 명령일 때, 배열의 크기 출력
        print(len(arr))
    elif command[0] == "get":
        # get 명령일 때, k번째 요소 출력 (1-based index)
        k = int(command[1])
        print(arr[k-1])  # 1-based index에서 0-based index로 변환하여 출력