clockTime = 0

"""
代表一条推文
"""
class Tweet:
    def __init__(self, tweetId):
        global clockTime
        self.time = clockTime
        clockTime += 1
        self.tweetId = tweetId

"""
代表一个用户
"""
class TwitterUser:
    def __init__(self, id: int):
        self._id = id
        self._tweets = []
        self._followeeIds = []

    def id(self) -> int:
        return self._id

    def getFolloweeIds(self) -> list:
        return self._followeeIds.copy()

    def postTweet(self, tweetId: int) -> None:
        self._tweets.insert(0, Tweet(tweetId))

    def getTweets(self) -> list:
        if len(self._tweets) < 10:
            return self._tweets.copy()
        return self._tweets[:10]

    def follow(self, followeeId: int):
        if self._id != followeeId and followeeId not in self._followeeIds:
            self._followeeIds += [followeeId]

    def unfollow(self, followeeId: int):
        if followeeId in self._followeeIds:
            self._followeeIds.remove(followeeId)

"""
代表整个推特
"""
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = []

    def _signUpNewUser(self, userId: int) -> None:
        self.users += [TwitterUser(userId)]

    def _findUser(self, userId: int) -> TwitterUser:
        nowUser = list(filter(lambda user: user.id() == userId, self.users))
        if nowUser == []:
            self._signUpNewUser(userId)
            nowUser = self.users[-1]
        else:
            nowUser = nowUser[0]
        return nowUser

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        nowUser = self._findUser(userId)
        nowUser.postTweet(tweetId)

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        nowUser = self._findUser(userId)
        feedTweets = nowUser.getTweets()
        for followId in nowUser.getFolloweeIds():
            feedTweets += self._findUser(followId).getTweets()
        feedTweets.sort(key=lambda tweet: tweet.time, reverse=True)
        feedTweetIds = []
        for feedTweet in feedTweets:
            if feedTweet.tweetId not in feedTweetIds:
                feedTweetIds += [feedTweet.tweetId]
        if len(feedTweetIds) > 10:
            feedTweetIds = feedTweetIds[:10]
        return feedTweetIds

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self._findUser(followerId).follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self._findUser(followerId).unfollow(followeeId)


twitter = Twitter()
print(twitter.postTweet(1, 5))
print(twitter.getNewsFeed(1))
print(twitter.follow(1, 2))
print(twitter.postTweet(2, 6))
print(twitter.getNewsFeed(1))
print(twitter.unfollow(1, 2))
print(twitter.getNewsFeed(1))
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
