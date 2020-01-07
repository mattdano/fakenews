import asyncio
from pyppeteer import launch
import pickle
from pyppeteer.network_manager import Response


import time
async def resp(res):
    print(res.text(), '\n')
    print(type(res))
    #pickle.dump(res,open('reply.pkl','wb'))
    return res.json()


async def send_article(article):

    browser = await launch({"headless": True})
    page = await browser.newPage()

    await page.goto('https://grover.allenai.org/detect')

    # go to textarea, click on that.
    await page.focus('textarea')
    print('Typing up message...')
    await page.keyboard.type(article)

    await page.click('button',{'waitUntil': 'networkidle0'})

    #pagecontent = await page.content('div.sc-dfVpRl')
    # stuff = page.on('response', lambda response: resp(response))
    # in the response, look for groverprob field for ans.

    #find objects with property resultProbability

    time.sleep(3)
    pagecontent = await page.content()


    return pagecontent


def sanity_check(article):
    if len(article) < 256:
        raise ValueError


def fake_new_scorer(article):
    try:
        sanity_check(article)
    except ValueError:
        print('Article too short. Try with more characters.')
        return None

    try:
        results = send_article(article)
        score_results = 0 #results['score']
        return score_results
    except Exception as e:
        print(e.args)
        print('Something went wrong')

        return None


if __name__ == '__main__':
    #fake_new_scorer('Some words here')
    test_text = '''Greta Thunberg, the Swedish schoolgirl who inspired a global movement to fight climate change, has been named Time magazine's Person of the Year for 2019.
The 16-year-old is the youngest person to be chosen by the magazine in a tradition that started in 1927.
Speaking at a UN climate change summit in Madrid before the announcement, she urged world leaders to stop using "creative PR" to avoid real action.
The next decade would define the planet's future, she said.
Last year, the teenager started an environmental strike by missing lessons most Fridays to protest outside the Swedish parliament building. It sparked a worldwide movement that became popular with the hashtag #FridaysForFuture.
Since then, she has become a strong voice for action on climate change, inspiring millions of students to join protests around the world. Earlier this year, she was nominated as a candidate for the Nobel Peace Prize.'''


    output = asyncio.get_event_loop().run_until_complete(send_article(test_text))

    print(output)