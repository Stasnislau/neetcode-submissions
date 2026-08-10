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
        posts.append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        authors = self.follows[userId] | {userId}
        for aut in authors:
            posts = self.posts[aut]
            if posts:
                heap.append((-posts[-1][0],posts[-1][1], aut, len(posts) - 2))
        heapq.heapify(heap)
        while len(res) < 10 and heap:
            next_time, post, aut, next_index = heapq.heappop(heap)
            res.append(post)
            if next_index >= 0:
                next_item = self.posts[aut][next_index]
                heapq.heappush(heap, (-next_item[0], next_item[1], aut, next_index - 1))


        return res

            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.follows[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
