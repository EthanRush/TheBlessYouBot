#Special thanks to Shantnu "shantnu" Tiwari for his tutorial series "Build a Reddit Bot" on pythonforengineers.com

#!/usr/bin/python
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

def idTracker():
    # Have we run this code before? If not, create an empty list
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    # If we have run the code before, load the list of posts we have replied to
    else:
    # Read the file into a list and remove any empty values
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    
    return posts_replied_to



# Select your desired subreddit
subreddit = reddit.subreddit('SUBREDDIT')
def main(posts_replied_to):
    for submission in subreddit.hot(limit=10):
     # If we haven't replied to this post before
        if submission.id not in posts_replied_to:
            # Search for cases representing a sneeze 
            if re.search("sneeze", submission.title, re.IGNORECASE) or re.search("achoo", submission.title, re.IGNORECASE):
                # Reply to the post 
                response = "Bless you u/" + str(submission.author) + "/n
                submission.reply(response)
                print("Bot replying to : ", submission.id)

                # Store the current id into our list
                posts_replied_to.append(submission.id)
                # Write our updated list back to the file
                with open("posts_replied_to.txt", "a") as f:
                    f.write(submission.id + "\n")
#Steps are the same for this but focusing on comments in the subreddit rather than post titles
    for comment in subreddit.comments(limit=500):
        if comment.id not in posts_replied_to:
            if re.search("sneeze", comment.body, re.IGNORECASE) or re.search("achoo", comment.body, re.IGNORECASE):
                response = "Bless you u/" + str(comment.author)
                comment.reply(response)
                print("Bot replying to : ", comment.id)

                posts_replied_to.append(comment.id)

                with open ("posts_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")


posts_replied_to = idTracker()
print posts_replied_to

while True:
	main(posts_replied_to)
