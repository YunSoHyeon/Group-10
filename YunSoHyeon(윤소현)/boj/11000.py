import sys
import heapq
input = sys.stdin.readline


cnt_of_class = int(input()) # 강의 개수 입력
time_of_class = []		 # 각 강의 시작 시간과 종료 시간을 저장할 리스트


for _ in range(cnt_of_class):
   time_of_class.append(list(map(int, input().split())))


time_of_class.sort() # 첫 번째 원소(시작 시간)을 기준으로 오름차순 정렬


start, end = heapq.heappop(time_of_class)
result = []
result.append(end)	# 첫 번째 강의의 종료 시간을 최소 힙 result에 추가
			# result는 현재 사용 중인 강의실의 종료 시간을 관리하는 최소 힙
			# 종료 시간이 가장 빠른 강의가 힙의 루트에 위치하게 됨
while time_of_class: # 남은 강의들의 강의실 배정
   start, end = heapq.heappop(time_of_class)
   if start < result[0]:	# 현재 강의의 시작 시간이 가장 빨리 끝나는 강의의 종료 시간보다 빠르면,
       heapq.heappush(result, end) # 새로운 강의실이 필요하므로 end를 최소 힙에 추가.
   else:		# 현재 강의의 시작 시간이 가장 빨리 끝나는 강의의 종료 시간보다 빠르지 않으면,
       heapq.heappop(result)	# 강의실을 재사용할 수 있으므로 기존 종료 시간 제거,
       heapq.heappush(result, end)	# 새로운 강의의 종료 시간 힙에 추가


print(len(result))
