# import
import heapq

'''
모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 
내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다. 

min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며
heap 내에서 가장 작은 값은 언제나 인덱스 0, 즉 이진트리 루트에 위치합니다.

주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 
1에 두번째로 작은 원소가 있다는 보장은 없다는 것입니다.
'''

# 최소 힙 생성
heap = []

# 힙에 원소 추가
# heappush는 O(logN)의 시간복잡도를 가집니다.
heapq.heappush(heap,4)
print(heap)

# 힙에서 원소 삭제
# 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제후, 그 값을 리턴합니다.
# heappop은 O(logN)의 시간복잡도를 가집니다.
''' 원소를 삭제하지 않고 가져오고 싶다면 heap[0] 인덱싱을 통해 가져올 수 있다.'''
print(heapq.heappop(heap))
print(heap)

# 기존 리스트를 힙으로 변환
# heapify는 O(N)의 시간복잡도를 가집니다.
heap = [4,1,7,3,8,5]
heapq.heapify(heap)
print(heap)

'''
[응용] 최대 힙 (max heap)
모듈은 최소힙 기능만을 동작하기 때문에 최대힙으로 활용하려면 요령이 필요합니다.
힙에 튜플(tuple)을 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 사용하여
각 값에 대한 우선 순위를 구한 후, (우선순위, 값) 구조의 튜플을 힙에 추가하거나 삭제하면 됩니다.
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다.
[응용] K번째 최소값/최대값
[응용] 힙 정렬

'''

# 최대 힙
''' 실제 원소값은 튜플의 1번째 자리에 저장되어 있으므로 1번 인덱싱을 통해 접근'''
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))
print(max_heap)

max_item = heapq.heappop(max_heap)[1]
print(max_item)


# 힙 정렬
def heap_sort(nums):
    heap=[]
    for num in nums:
        heapq.heappush(heap,num)
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

print(heap_sort([4,1,7,3,8,5]))