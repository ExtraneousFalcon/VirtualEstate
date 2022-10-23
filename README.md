# Virtual Estate
# Inspiration
The recent volatility in our economy due to COVID and inflation have inspired us to dig deep into what causes them. We wanted to understand how to leverage fundamental analysis and technical knowledge to predict this volatility and successfully invest during these times. Our curiosity led us to build this project to aid us in our pursuit of smarter investing.


# What it does
Our platform provides an easy to use tool that streamlines the process of identifying high return real estate investments, leveraging the high volatility within the markets. We provide key information including a combination of buy/sell signals using machine learning, volatility indicators, and pivotal real estate investment indicators. 

# How we built it
We created Virtual Estate through the Django framework incorporating Python, Javascript, HTML, and CSS. In addition, we used the Scikit Learn Library to develop the machine learning model using the Kaggle dataset of New York Housing - Zillow API. We were also able to host the web application on Heroku.


# Challenges we ran into
This was the first time that we all trained a Neural Network Machine Learning model from scratch using Scikit Learn at this magnitude. We were initially faced with the challenge of finding a dataset on house features vs. prices that gave insightful information through several thousand entries. Additionally, the process of actually training the Neural Network turned out to be quite tedious with several hyperparameter tunings of learning rates, hidden layer configuration, and other properties that ultimately proved to be very useful. Furthermore, Heroku posed several complications to host our web application as its integration with Django was quite complex. Lastly, one of the most time consuming processes of our entire hack was understanding the real estate landscape through in-depth research and talks with industry professionals to determine which key factors would ultimately benefit true value to an investor and give them an edge in the market. 

# Accomplishments that we're proud of
Primarily, we are pleased to showcase that our Machine Learning Model predicts the value of a property based on creative and fundamental features with a r2 score of 0.8, achieving an exceptional level of correlation between feature inputs and model price predictions, using over 50,000 entries of data. We are also proud to say that we were able to strategically leverage the volatility of the real estate market using a combination of Customer Price Index, Housing Affordability Index, and Interest Rate. Furthermore, we incorporated advanced investment factors including Gross Rent Multiplier, One Percent Rule, Cap Rate, Net Income after Financing, and Cash on Cash Return to provide a new insight to a property’s investability. At the heart of our platform, we are proud to combine the technical aspects of our project with modern UI/UX designs to create the perfect client/user centric solution! 


# What we learned
Before simply throwing technology at any problem, it is crucial to uncover the black box that resides within the unique landscape and situation of the environment. Understanding this critical component of any project through smart research enables you to come up with creative ideas from a technological and ideation perspective. Although the realm of real estate was new for each and every member on our team, we had the genuine interest to understand the needs of the investors and people in this market to create an amazing real estate investment tool! 
In addition, we all definitely had a newfound appreciation for every individual’s specialization on the team and the power of leveraging each and every individual’s potential on the team! Ramya designed and implemented an amazing and accessible user interface, Rithesh led the development of an innovative machine learning model, Sai served as the key member for connecting our pieces through a central server, and Sohum played the important role of integrating external APIs and leading discussions on market research. The beauty of Innovation truly stems not from an individual petal from the entire flower!

# What's next for Virtual Estate
We hope to expand the modularity of virtual real-estate from examining individual properties to the hottest properties in a single zip-code. We also hope to expand the market from New York to other areas across the country and gather morre data sets to find new features that are innovative to predict the value of a property such as the average income of a neighborhood, tax rates

![home](https://user-images.githubusercontent.com/91358365/197379596-ffcdf972-1480-40a2-9c23-f600d7c513ca.png)
![dashboardSearch](https://user-images.githubusercontent.com/91358365/197379595-be7f8b5e-92cb-4429-b8d3-8bf2e2cc074b.png)
![buySellDashboard](https://user-images.githubusercontent.com/91358365/197379594-2d3f1bb0-7a65-45f1-9dd0-660dccc10348.png)
![volatilityDashboard](https://user-images.githubusercontent.com/91358365/197379598-88715a19-3cce-4567-bc72-b50034e43006.png)
![investmentFactorsDashboard](https://user-images.githubusercontent.com/91358365/197379597-41c5f9cc-09be-484c-974f-a4737d317918.png)

