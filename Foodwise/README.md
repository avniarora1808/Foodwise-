# Foodwise

## Inspiration

As high school students, we are always busy, hungry, and typically not very experienced in the culinary arts. Our team was motivated to create a solution that can help us find good healthy recipes while not sacrificing study time. The ultimate goal is to improve both our mental and physical health, by relieving the stress generated from the indecision of what to eat. Other benefits of using the app include encouraging home-cooking, being more conscious of meals, and learning the skills of cooking. With Foodwise, there will be no more of opening the fridge and spending time staring blankly at the items inside that could be used for learning instead.

## What it does

Welcome to Foodwise; an interactive adventure where we suggest meals based on your personal needs, preferences, and available ingredients! Save yourself the hassle of buying expensive food components and looking through frustrating recipe lists using our reliable, easy to use software (with exact, simplified measurements and instructions). Our website offers 3 methods to input some of your current ingredients: photo detection, manual input, paragraph input. Photo detection allows users to upload an image of their fridge and our program will identify 5 ingredients in the image. Manual input submits a form of the ingredients entered by the users while paragraph input identifies ingredients based on key terms from the input. After processing the given ingredients, Foodwise returns a number of meals with information such as recipes, calories count and serving size.

### Features
It helps you stay healthy with it's recipe suggestions, and gives you an incentive to cook at home. It relieves stress with simple and easy to use recipes, and gives tips about healthy eating. It helps you make conscious decisions about what you eat, and teaches you about culinary arts and famous recipes to easily cook at home. It helps save energy, since one image and a click is all it takes to know what you want to make, instead of searching forever in the fridge. By doing so, you also don't waste food by eating fresh, and it thus reduces your carbon footprint. 

## How we built it

We used HTML/CSS/JS for the frontend, and Flask/Python for the backend. We leveraged the Edaman recipes API to serve live recipe data, and ran the code on an nginx live server hosted on an Azure VM with a custom domain. For the machine learning, we used a clarifai multiclass visual classifier model trained on a custom dataset, and using Yet Another Keyword Extractor to perform natural language processing and extract keywords and sentiment predictions from a piece of text. 

## Challenges we ran into

As a group, we used ssh to work in the same repository, instead of using github or vscode live share. Although the server was hard to set up and crashed a few times, it proved very useful during collaboration. We had some issues connecting the frontend and backend, especially since we each worked on different parts, but we ended up planning out how to access a certain part of the code to not compromise any merge issues. 
The frontend CSS had to be changed many times to match the changing HTML, and sometimes merge issues would cause chunks of CSS to be deleted, so we decided to run/cache locally and resolve any merge issues through VSCode. Through this, we were able to complete everything on time. 
We had trouble working with Flask sessions, requests, and dependencies, but we ended up getting the configuration to work very well. We also had issues serializing and converting between inputs for the API calls. 
The AI model had to be trained to improve its accuracy, since it was difficult to fit the model over a different dataset, but it ended up working. Another challenge was finding a good keyword extraction model that would give us accurate prediction values. 
Finally, the deployment was also quite difficult as the wsgi production server needed to run smoothly with low latency (while also making Azure collaborate with it). Setting up the dependencies and redirecting to a custom domain DNS also took quite a while. However, this proved useful in the long run as having a stable ssh terminal production server let us run debug tests and restart the server to test new features extremely easily. 

## Accomplishments that we're proud of

We are proud that we were able to produce a working and sleek solution to a common stress-inducer. We are happy that we were able to leverage an AI model and API in our project, as well as get a secure nginx deployment server running on a custom domain. 
Overall, we are proud of our teamwork, especially considering that nobody knew everyone else before the hackathon. Despite the obstacles we encountered throughout our journey, we were able to create a meaningful project together and have fun.

## What we learned

We learned to brainstorm ideas in a short amount of time and be innovative individuals that can improvise and work through issues together when we come to a dead end. We learned how to quickly train AI models, as well as leverage APIs to get crucial data. We learned how to connect the frontend and backend when doing full stack web development, as well as using (Linux) virtual machines and deploying onto an nginx server. 

## What's next for Foodwise

Foodwise can be improved in many ways. More features and ways to get recipes can be added. The accuracy of the ML and NLP models can be increased (by training on enhanced datasets). The frontend can be prettified further, and the full stack web app can be scaled to include a user base (and database) if needed, perhaps with migrations of the deployment server. Foodwise can also become an app or chrome extension, to increase accessibility and outreach. 

