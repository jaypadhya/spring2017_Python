midterm/que1/

# 1)CEO EMAIL ANALYSIS:
What are we analysing:
- Analysis over emails from CEO Lay K to go through ALL folders and collect all the words. Then perform a word count on it and store 
as an image in the ouput folder. We also iterate over the headers to locate the common subject and go in depth of the body. 

# INFERENCE: WE ITERATED OVER THE CEO's HEADERS to know what the most common subject was and the most common words in the email body. The most common subject was a demand from many users to return back the cash from scandal and the most common words in email body included Enron, million,bankrupcy.

# 2)EMAIL NETWORK ANALYSIS: 
What are we analysing:
- Email Network Analysis to find the number of emails sent and received per user to understand the flow of communication over the network.

# INFERENCE: We can now analyse how many emails were sent and received by each employees. This analysis helps to understand the communications email chains between employees and helps us understand the people receiving highest sent emails and highest receipient emails. The csv file gives the names of users along with their emails sent and received by employee name

# 3) SUSPICIOUS EMAIL ACTIVITIES:
What are we analysing:
- Analysis over Suspicious activity over email exchange over dates.
Ideally any major activity can be noted with the influx of information over email - these activities include release of IPO, change of
CEO or major events. When no such major event is occuring and still there is a pike in communication over emails, then there can be
a suspicioun over company activity. 

# INFERENCE:  We can clearly see that there was a pike in October 2000 till mid 2001 which is where the scandal was about to occur. Thus without any major activity going over - like release of IPO, change of CEO and if the company's internal communication shoots up, there is some suspicious activity which can be inferred. 


midterm/que2/

# 1) API Call to Articles API for Proving Zipf Law over huge dataset:
What are we analysing:
- We iterate over all the articles from 1900's to 2016 and collect all the articles from NY Times to see how much data can be generated.
The content would be extremely massive and we would see if the ZIPF law holds true under such circumstances as well.

# INFERENCE: Hence we have proven about ZipF Law that holds true after iterating over so many articles across a long range of dates and fetching the words by rank. 
The csv file is submitted for exact count as well and the image is attached following Zipf Law.

# 2) API Call to Articles API for Technologist Popularity:
What are we analysing:
We can conclude that when technologists like Bill Gates and Mark Zuckerberg speak on various issues, their popularity depends on 
which topics they are covering. 
- We iterate over all the articles from 1900's to 2016 and collect all the articles from NY Times to see how much data can be generated.
We pick out words like Mark ZUckerberg and Bill Gates to see how their names are associated with the content. They were associated
with either community service (Mark Z) or statements on politics/cities (Bill Gates). Later the article distcribution on both were 
calculated to find an interesting inference.

# INFERENCE: In our case, Zuckerberg spoke more on community imporvements and Bill Gates spoke more on Politics. 
Bill gates gained due popularity indicating that NYTimes writes more on politics over community improvements.  


# 3) API Call to Community for most recommended user comments with count/upvotes and geography:
What are we analysing:
After using Community API, we iterate over the data to find out regions, recommended comments with counts/upvotes by different users.

# Inference :Geographically, There seems to be many users from Boston who are often commenting and getting upvotes indicating a literature rich population from Boston. The advertising media can target on the basis of location. Also, from the wordcloud, most users use hyperlinks to justify their points and hence NY Times should target advertisers like bitly which can condense the URL shared and users can make concise comments. Also, words like Need,Trump, Economic, negative, overspending suggests that people are inclined on talking about politics and economics.

