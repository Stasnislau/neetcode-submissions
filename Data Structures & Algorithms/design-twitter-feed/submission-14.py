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

        for uid in self.follows[userId] | {userId}:
            tweets = self.posts[uid]
            if tweets:
                time, tweetId = tweets[-1]
                heap.append((-time, tweetId, uid, len(tweets) - 2))
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, tweet, uid, next_index = heapq.heappop(heap)
            res.append(tweet)
            if next_index >= 0:
                next_time, next_tweet = self.posts[uid][next_index]
                heapq.heappush(heap, (-next_time, next_tweet, uid, next_index - 1))

        return res

            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.follows[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
