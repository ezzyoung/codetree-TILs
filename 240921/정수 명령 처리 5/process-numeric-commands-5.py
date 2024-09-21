k = []  # 리스트 초기화


a = input().split()  # 입력을 공백 기준으로 나누어 처리

if a[0] == "push_back":
    k.append(int(a[1]))  # 두 번째 요소를 리스트에 추가
elif a[0] == "pop_back":
    print(k.pop())  # 마지막 요소를 제거하고 출력
elif a[0] == "get":
    index = int(a[1])
    print(k[index])  # 해당 인덱스의 값을 출력
else:
    print(k.append(a))