# Game Recommendation System
project for course ECE 6254 19 Spring  
Team member: Weihua Zhu, Chengxi Yao, Wei Zhao, Xiangwei Sha

# Project Proposal
## Project Summary
Instructions: Using a maximum of one page, the first page of your proposal should summarize the project by clearly indicating what you plan to do. You should include sufficient background so that anyone taking this class should be capable of understanding (at a high-level) what you are planning on doing. The goal here is to convince me why the problem you are addressing is important and why the outcome of your project will be interesting.  

We plan to do a video game recommendation machine learning system, given the input from users of their several answers to the survey or personal interests. The application is based on datasets in the reference section, combined with the data we scraped on our own(mostly to fill in the missing data for year 2017 and 2018). The combined dataset would then contain all video games on PC, XBOX, PS, Nintendo, etc. for 80s to most recent ones, including the genre, different region sales data, and user ratings.  

We would build machine learning model on top of the dataset, visualize the data and implement a recommendation application. The problem we are addressing is important is that, in entertainment industry, although the movie or music recommendation system built with machine learning are already mature, e.g., Netflix personalized movie recommendation based on user's watching history and Apple music recommendation based on user's survey and playlist history, the game industry still lacks this kind of similar recommendation for players. Different from movie or music, the cost for games are much higher and requires more time devoted in, so especially for new players that just stepped into game world, he/she might not have abundant experience in choosing the suitable game. Also another difference is that most of the games are also platform dependent, so recommendation based on specific platform is also an important factor in game recommendation models. The motivation of the project is to make gamers, and especially new games life easier, with more than one million games currently in the world, it would save gamer so much time and money to just provide with them a list of top recommendations based on their preference or the games that they love.

The outcome of our project will be a machine learning model for similar top games recommendation system, and a web application on top of this to visualize our data, accept inputs from users and provide output list of top recommendations back to users by going through our backend game recommendation machine learning model. The outcome will be insteresting in that the players could get instant feedback/suggestions on their next list of games to buy, and provide eshop links for them.


## Detailed Project Description
In this section you should provide a more detailed description of the necessary background and specific objectives of your project. Include citations to any papers/books you are planning on building on, and feel free to include any preliminary re- sults if you happen to already have them. This section should be at most three pages of text (including references/figures) and is intended to give you a bit more room to fully flesh out your ideas if you cannot fit them entirely within the one page summary. You should treat the summary as a stand-alone document, and the detailed description should not be a “follow-up” section but a full, self-contained, description of your project. It is fine to repeat some of the language from the summary if you would like. You should also feel no pressure to make this three full pages. If you can say what you want to say in one or two pages, then this might not be very different from the summary, and that is fine.  


## List of tasks/collaboration plan
In this section I would like you to provide an enumerated list of the tasks you believe will be required to successfully complete the project. Tasks can include learning about pre-requisite background subjects, reading specific papers, implement- ing particular algorithms, acquiring/processing a data set, or anything else that you believe will be necessary for the project. You may also include tasks related to preapring/printing the final project poster and writeup. For each task, include the following information:  
– Task: A detailed statement of the task to be accomplished. Your statement should ideally be specific enough that you will be able to clearly measure when it has been finished. “Read papers X and Y” is better than “Learn about field Z”.  
– Leader(s): Which team member(s) will be primarily responsible for accomplishing this task. (It is fine if all team members are planning to contribute to all aspects of the project, but please designate one or at most two people to be the leaders for each task).  
– Deadline: A tentative deadline for when you would like to have this task accomplished.    
– Importance:Abriefstatement(canbeonlyasentenceortwo)astotheoverallimportance of this task. Some tasks are critical, meaning that it is hard to see how the project will be complete without it, whereas other tasks are more “optional” items that you would like to get to if you have the time. For each task, state if it is a critical or optional task. If later tasks depend on it as a prerequisite, state this.  
– Potential challenges: A list of things that you think might “go wrong” and what, if anything, you plan to do to avoid/overcome these challenges and/or what you would do if you can’t get past them.  
There is no page limit for this section, but I’m not expecting more than a page or so.  

# Reference links
Dataset:  
https://www.kaggle.com/gregorut/videogamesales the base one,  
https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings   based on vgcharts and metacritic  
https://www.kaggle.com/kendallgillies/video-game-sales-and-ratings  
https://www.kaggle.com/juttugarakesh/video-game-data  
https://www.kaggle.com/egrinstein/20-years-of-games#ign.csv based on IGN data  

Web source:  
VGcharts, metacritic, IGN  

Crawler:  
Metacritic Scraper: https://github.com/wtamu-cisresearch/scraper  
VGchart Scraper: https://github.com/GregorUT/vgchartzScrape  
