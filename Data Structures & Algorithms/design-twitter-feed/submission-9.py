from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(deque)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        posts = self.posts[userId]
        if len(posts) > 9:
            posts.popleft()
        posts.append((-self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.follows[userId] | {userId}:
            posts = self.posts[uid]
            for i in range(len(posts)):
                heap.append(posts[i])
                if i == 9:
                    break
        heapq.heapify(heap)
        res = []
        i = 0
        while i < 10 and heap:
            res.append(heapq.heappop(heap)[1])
            i += 1
        return res

            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.follows[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.follows[followerId]:
            return 
        self.follows[followerId].remove(followeeId)
        
