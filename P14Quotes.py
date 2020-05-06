#SparkmanP14
#Programmer: Bailey Sparkman
#Email: bsparkman@cnm.edu
#Purpose: Generates a random quote based on users choice of category
#open with python 2 NOT 3!!!

import random
##import twython
##from twython import Twython
##from auth import ( #add twitter API to upload quote to Twitter!
##    consumer_key,
##    consumer_secret,
##    access_token,
##    access_token_secret
##    )
##twitter = Twython(
##    consumer_key,
##    consumer_secret,
##    access_token,
##    access_token_secret
##    )


def Welcome():
    print '''
    Welcome! Please enter the category that you would
    like your quote to be about (friends, authenticity,
    kindness, or love)! Enter 'sources' or 'collection'
    for more!
    '''

quoteList = []

def friends(): 
    f = open('friends.txt','r')
    line = f.readlines()
    quote = random.choice(line)
    print quote 
    quoteList.append(quote)
def authenticity():
    f = open('authenticity.txt','r')
    line = f.readlines()
    quote = random.choice(line)
    print quote
    quoteList.append(quote)
def kindness():
    f = open('kind.txt','r')
    line = f.readlines()
    quote = random.choice(line)
    print quote
    quoteList.append(quote)
def love():
    f = open('love.txt','r')
    line = f.readlines()
    quote = random.choice(line)
    print quote 
    quoteList.append(quote)
def sources():
    f = open('sources.txt','r')
    for source in f:
        print source
        print
def collection():
    print "Here is a list of quotes you have seen so far:\n"
    for quote in quoteList:
        print quote

##def TwitterPost(userchoice):
##    upload = raw_input ("Would you like to upload your quote to Twitter? (y/n)")
##    if upload == 'y':
##        userchoice = twitter.update_status(status = userchoice)
##    else:
##        print ("ok")
#Main Program:
Welcome()
doanother = 'y'
while doanother == 'y':
    userchoice = raw_input("What would you like your quote to be about? ")
    print
    if userchoice.lower() == "friends":
        friends()
        
    elif userchoice.lower() == "authenticity":
        authenticity()
        
    elif userchoice.lower() == "love":
        love()
        
    elif userchoice.lower() == "kindness":
        kindness()
        
    elif userchoice.lower() == "sources":
        sources()
        
    elif userchoice.lower() == "collection":
        collection()
    else:
        print "I did not understand that, please try again! \n "

    doanother = raw_input ("Would you like to get another quote? (y/n) \n")
    
print "\nThank you for using my random quote generator!!"
