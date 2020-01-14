#Fake news

When I first got told of this, details were vague: "Detect fake news." Unsolved by anyone. Even Facebook and Google. 

You cannot use any of the examples currently around. Those are just datasets generated for a kaggle toy problem. 

### REAL LIFE IS WAY HARDER.


What I started looking at first: 
1. Source is completely made up, by a machine.
Used a pre-trained GAN model called grover by the Allen insitute to distingush human and computer generated articles. 

Hijacked their API to score text, [0-1]. No point recreating their demo...

-----------------

Then Chris said: 

 "featured in a session we were giving to Fidelity...
Basically if they want to use NLP on text articles etc in their investment decisions, how can they be sure the source is legitimate"


"Source is legitimate"
1. Altered the facts
2. Untrustworthy source
3. Fake source. Reposting
4. Heavy bias interpretation of the facts to conclude something else. 
5. Actor serves a different page to you, knowing you work for company X. (Just use a VPN to double check the content is the same)
6. Just straight up lies.

Approaches: 
- 'Legit' sources will have more backlinks, so the pagerank method would be fine. Also can make use of metrics, hits/month etc to tell. Score a domain on their popularity. See: Alexa, google zeitgeist etc
- Detect and warn on potenitally click baity signals. 
- Find simiar articles, compare differences. Are Facts from A same as Facts from B. 

Issues:

-- News/content is dynamic, Fact A won't still be true. 
-- Don't have access to enough surface of the web, we're not google
-- Sentence understanding sentiment is really hard, could use some deep models like BERT. But those are large and unwieldy. 
-- Sources behind paywalls