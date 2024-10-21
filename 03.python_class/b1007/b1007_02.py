numbers = [273,103,5,32,65,9,72,800,99]

# 100 이상 값만 출력
# for num in numbers:
#   if num >= 100:
#     print(num)

# 크기 순으로 정렬 방법
# numbers.sort()     # 순차 정렬 - 낮은 수부터 출력
numbers.sort(reverse=True)  # 역순 정렬 - 높은 수부터 출력(자리수 비교 O)
# numbers.reverse()  # 순서를 역순으로 정렬
print(numbers)

