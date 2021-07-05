import heapq

def solution(jobs):
    answer = 0
    i, last_time, now = 0, -1, 0
    heap = []
    while i < len(jobs):
        
        # 현재 시간 이전에 요청된 작업 힙에 추가
        for job in jobs:
            if last_time < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        
        # heap에 요청 작업이 추가되면 
        if heap:
            cur_job = heapq.heappop(heap)
            last_time = now
            now += cur_job[0]
            answer += (now - cur_job[1])
            # 다음 요청
            i += 1
        # heap에 요청 작업이 추가되지 않았으면 시간만 흐른다
        else:
            now += 1
        
    return answer / len(jobs)
