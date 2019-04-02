# Video Game Recommendation
project for course ECE 6254 19 Spring  
Team member: Weihua Zhu, Chengxi Yao, Wei Zhao, Xiangwei Sha

# Project Proposal
## Project Summary
We plan to build a video game recommendation system with the machine learning algorithm based on answers to several survey questions or our users’ personal interests. Our recommendation system is trained on the datasets in the reference section, combined with the data we scraped on our own (mostly to fill in the missing data for the year 2017 and 2018). The combined dataset would then contain all video games on PC, XBOX, PS, Nintendo, etc. from the 1980s to most recent ones, including the genre, regional sales data, and user ratings.  

We would build a machine learning model on top of the dataset, visualize the data and implement a recommendation application. Movie or music recommendation systems built with machine learning are already mature in the entertainment industry, e.g., Netflix personalized movie recommendation based on user's viewing history and Apple music recommendation based on user's survey and playlist history. However, the game industry still lacks such kind of similar recommendation system for players. This is why we think the problem we are addressing is important. Unlike movie or music recommendation, users in game recommendation systems do not have a clear idea of what kind of games they will like. The money and time cost in selecting the right games is much higher especially for new players who just step into the game world and lack experience. Another difference is that most of the games are platform dependent, which means we must implement our game recommendation based on specific platforms. The motivation of the project is to make gamers, especially new gamers’ life easier when they are faced with over one million games currently available in the world. It would save gamer so much time and money if we can just provide with them a list of top recommendations based on their preferences.  

The outcome of our project will be top games recommendation system exploits the machine learning algorithm and a web application on top of this to visualize our data. It can accept inputs from users and provide a list of top recommendations back to users by running our backend game recommendation machine learning model. The outcome will be interesting in that the players could get instant feedback/suggestions on their next list of games along with their shopping links.


## List of tasks/collaboration plan
Tasks:  
Implement data crawling of the 2017 and 2018 video game sales data based on the existing crawler. 
Importance: Critical but nice-to-have if the data crawling takes much time, fundamental of completeness of dataset.  
Leader: Weihua Zhu.  
Deadline: 4/3/19.  
Potential challenges: API expirations or degradations.  
Solution: if the API has been upgraded, we would rewrite the code based on the new version, if there is no API supported and it is also non trivial to write a new crawler that fixed the problem, we would avoid this first and finish the project based on the dataset without 2017 and 2018 years’ data, and then finish the crawling and feeding in the new data if we have time.  

Build a Decision tree based machine learning model for game recommendation, reads paper [2] and relevant papers, and finish model measurement.  
Importance: Critical, dependencies: task 1. One key approach and algorithm for recommender systems.  
Leader: Xiangwei Sha. Deadline: 4/15/19.  
Potential challenges: Specific branching criterions choice, the way to measure whether the recommended top K list for users has high accuracy and coverage.  
Solution: Parameter tuning. Potentially measure the recommendation list based on users’ review data on platforms such as Steam.  

Build a graph based nodes and relationships recommendation model for game recommendation, reads paper[3] and relevant papers, and finish model measurement.  
Importance: Critical, dependencies: task 1. Another key approach and algorithm for recommender systems, to compare with the decision tree results.  
Leader: Wei Zhao.  
Deadline: 4/15/19.  
Potential challenges: Need to implement Neo4j which is a graph database to represent and store data.  
Solution:  Learn Neo4j through sample projects on Neo4j website.  

Implement the item-based filtering, given conditions from the user input, filter out the results, reads paper[4] and relevant papers, and finish model measurement.   
Importance: Critical, dependencies: task 2 and 3. Fundamental of personalized and customizable game recommendation.  
Leader: Chengxi Yao.  
Deadline: 4/20/19.   
Potential challenges:  Due to limited number of samples and large number of features, overfitting may occur.  
Solution:  We can merge the random subspace method and support vector machine classifier to elude over-fitting.  

Web application implementation. 
Importance: Optional/Nice-to-have, dependencies: task 2, 3 and 4. Given the timeline of our project, our main focus would be on the recommendation system model/backend logic, and measurement of our system. If we have time, we would do the frontend web app for our project. 
Leader: Weihua Zhu.  
Deadline: 04/28/19.  
Potential challenge: Limitation of timeline.   
Solution: Do the web app in last step, and focus on basic user interfaces using simple HTML/javascript at the first stage.  

Final Poster presentation and project report. 
Importance: Very critical, finish all deliverables and presentation, dependencies: task 1,2,3,4 and 5(optional). 
Deadline: 5/2/19. 
Leader: Chengxi Yao 
Potential challenges: Figuring out best way of visualizing our results. 
Solution: Provide live personalized recommendation tests of our application at the presentation. Provide meaningful charts corresponding to our results to make the results more visible and make sense. 

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
