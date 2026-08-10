class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [[0, i] for i in range(n)]
        heapq.heapify(rooms)
        counts = [0] * n
        for meet in meetings:
            while rooms and rooms[0][0] < meet[0]:
                room = heapq.heappop(rooms)
                heapq.heappush(rooms, [meet[0], room[1]])
            room = heapq.heappop(rooms)
            room[0] += meet[1] - meet[0]
            counts[room[1]] += 1
            heapq.heappush(rooms, room) 

        return counts.index(max(counts))