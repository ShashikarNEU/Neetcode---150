# Have a hash map for followers and posts acc to each user
# Follow and unfollow logic is simple -> add and remove from the hash map - followers
# for news feed, collect the followers of the users, then get the posts, for the timings of the posts
# store it in the heap [-time, tweetId] (max heap) and pop it till the heap is empty or 10 posts are reached

# Do the max heap push inside the getnewsFeed method, don't do it in post tweet [IMP]
# Using the hashmap for posts is efficient and we can only add the followers posts only
# Using a list means we have to scan every post which is inefficient

from collections import defaultdict
import heapq
from typing import List
class Twitter:
    def __init__(self):
        self.userPostsMap = defaultdict(list)
        self.followeeFollowMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.userPostsMap[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        # To get all users userId has followed and push it into a max heap
        if userId in self.followeeFollowMap:
            followers = self.followeeFollowMap[userId]
            for user in followers:
                posts = self.userPostsMap[user]
                for timeStamp, tweetId in posts:
                    heapq.heappush(max_heap, (-1*timeStamp, tweetId))
        
        # To get userId posts and push to the max heap
        self_posts = self.userPostsMap[userId]
        for timeStamp, tweetId in self_posts:
            heapq.heappush(max_heap, (-1*timeStamp, tweetId))
        
        res = []
        while max_heap and len(res) < 10:
            _, tweet_id = heapq.heappop(max_heap)
            res.append(tweet_id)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followeeFollowMap[followerId]:
            self.followeeFollowMap[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followeeFollowMap:
            if followeeId in self.followeeFollowMap[followerId]:
                self.followeeFollowMap[followerId].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Other Attempt
class Twitter:
    def __init__(self):
        self.UserPostsMap = defaultdict(set)
        self.UserFollowsMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.UserPostsMap[userId].add((-1 * self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:
        userList = set()
        res = []
        if userId in self.UserFollowsMap:
            userList = self.UserFollowsMap[userId]

        # Fetching own user posts also
        userList.add(userId)
        max_heap = []

        for user in userList:
            if user in self.UserPostsMap:
                posts = self.UserPostsMap[user]
                for post in posts:
                    max_heap.append(post)
        
        heapq.heapify(max_heap)

        while len(res) < 10 and max_heap:
            _, tweetId = heapq.heappop(max_heap)
            res.append(tweetId)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.UserFollowsMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.UserFollowsMap:
            if followeeId in self.UserFollowsMap[followerId]:
                self.UserFollowsMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)