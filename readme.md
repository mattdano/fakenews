Fake news detection. 

#Why 
Because Boris said so.

# Background

A few groups have looked into this. AllenAI are probably the most advanced with their work, plus they have a demo and released pretrained tensorflow models.  

# Plan
I do not plan to run any of the tensorflow models, no need becuse they have a web demo of it all!

Going to take the public facing demo from the Allen Institute for Artificial Intelligence and reuse a lot of it for our demo. 

https://grover.allenai.org

Can't just take the api calls as you would hope due to cross site blocking, so idea is to just use puppeteer to interact and feed it data. Some python backend to handle all of this, and a web mudano themed front end.

Front end should show the generated news, along side some human ones. 

Make it fun by allowing the user to guess which fininal articles are human or machine generated. 

## Todo:
In order of usefulness:

 - Some function to score a new article: between [0-1] , where 1 is 100% confidence of being ML generated fake news.
 
 - Allow aribtary news text to be scored.  

 - Generate some more fake news examples specifc to finance. 
 
 - Make web front end to display results and examples
 
 - Make the front end fun as a game or some useful client interactions