import sys
input = sys.stdin.readline


test_case_count = int(input())


for i in range(test_case_count):
   day = int(input())
   stocks = list(map(int, input().split()))
   sorted_list = sorted(stocks, reverse=True) # 주식 가격 내림차순 정렬




   if sorted_list == stocks:	# 주식이 이미 내림차순으로 정렬되어 있다면,
       print(0)			# 더이상 주식을 팔지 않는 것이므로 수익은 0
   else:
       income = 0
       while len(stocks) != 0:	# 주식 가격 리스트가 빌 때까지 반복
           max_index = stocks.index(max(stocks)) # 현재 리스트에서 가장 큰 주식 가격 찾기
           for_income = stocks[:max_index]	# 최대 주식 값보다 작은 주식들 저장
           max_stock = max(stocks)		
           stocks = stocks[max_index + 1:]	# 최댓값 이후의 주식 가격으로 갱신
           for j in for_income:
               income += (max_stock - j) 	# 수익 더하기 
       print(income)
