import praw
import pdb
import re
import os




reddit = praw.Reddit('/Users/Eid/anaconda/lib/python2.7/site-packages/praw') #Part of Reddit API
if not os.path.isfile("posts_replied_to.txt"):  #Creates text file to paste replied links
	posts_replied_to = []

else:
	with open("posts_replied_to.txt","r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None,posts_replied_to))



subreddit = reddit.subreddit('All') #designate the subreddit to reply to
for submission in subreddit.new(limit=10): #loops through the submissions
	 firstID = submission.id #current posts ID
	 results = subreddit.search(submission.title,sort="relevance", syntax=None)
	 for currentResult in results:
	 	 if(firstID != currentResult.id): # to avoid linking back the same post. 
	 	 	submission.reply("Similar posts to yours: http://www.reddit.com/" + currentResult.id + "\n" + "I am a bot and this action was performed automatically.")
	 	 	print("Currently replying to: " + submission.title)
	 	 	if submission.id not in posts_replied_to:
	 	 		print("hi")
	   			posts_replied_to.append(submission.id)
	   			f.write(submission.id + "\n");
	   		break
	

	   	              	



















	   	   
	   	   






