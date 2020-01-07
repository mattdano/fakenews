
import requests
import json

article_text = "On Friday the legislature of Taiwan, the Legislative Yuan, voted 66 to 27 to legalize same-sex marriage, seven days ahead of the two-year deadline issued by the country's Constitutional Court in 2017. This would make Taiwan the first country in Asia to legally recognize unions between same-sex couples. The law is to take effect late this week.\nThe Legislative Yuan debated three competing bills, and selected the one posed by the country's cabinet, which used the word \"marriage,\" over the two posed by conservatives, which used the terms \"same-sex family relationship\" and \"same-sex union.\" The selected bill does not offer same-sex couples all the same rights as their heterosexual counterparts; there are limits on adoption rights and marriage with foreigners.\nJennifer Lu of Marriage Equality Coalition Taiwan said, \"[I]t's still not full marriage rights; we still need to fight for co-adoption rights, and we are not sure about foreigner and Taiwanese marriage, and also gender equality education.\"\nThe Taiwanese government held a referendum in November 2018, allowing the population to vote on same-sex marriage, and 67% came out against.\nXiaogang Wei of the Beijing Gender Health Education Institute commented on the Legislative Yuan's decision: \"The Chinese government has pointed to cultural tradition as a reason for same-sex marriage being unsuitable in China. But the decision in Taiwan, which shares a cultural tradition with us, proves that Chinese culture can be open, diverse and progressive.\"\nIn mainland China, which claims sovereignty over Taiwan, homosexuality is technically not illegal, but late last year a same-sex erotica author was sentenced to ten years in prison, and same-sex marriage is not recognized.\nIn 2017, Taiwan's Constitutional Court, which rules on constitutional matters, said not allowing gay citizens to marry constituted \"different treatment\" incompatible with the constitution. The decision prompted objections from conservatives opposing recognition of gay marriage."
domain=""
date=""
authors=""
title=""
target="discrimination"


payload = dict(article=article_text, domain="",date="",authors="",title="",target="discrimination")
print(json.dumps(payload))
#exit()



response = requests.post(
    'https://discriminate.grover.allenai.org/api/disc',
    json=json.dumps(payload),
    headers={'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'https://grover.allenai.org' ,
            'Content-Length': '2117',
            'Accept-Language': 'en-gb' ,
            'Host': 'discriminate.grover.allenai.org' ,
            'User-Agent': ''''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15''' ,
            'Referer': '''https://grover.allenai.org/detect''' ,
            'Accept-Encoding':'gzip, deflate, br',
            'Connection': 'keep-alive' ,
             },
)

print(response.text)
print(response.text)


exit()
#this curl command works.
# just need to implement this in python requests.
'''


curl 'https://discriminate.grover.allenai.org/api/disc' \
-XPOST \
-H 'Accept: application/json, text/plain, */*' \
-H 'Content-Type: application/json;charset=utf-8' \
-H 'Origin: https://grover.allenai.org' \
-H 'Content-Length: 2117' \
-H 'Accept-Language: en-gb' \
-H 'Host: discriminate.grover.allenai.org' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15' \
-H 'Referer: https://grover.allenai.org/detect' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Connection: keep-alive' \
--data $'{"article":"On Friday the legislature of Taiwan, the Legislative Yuan, voted 66 to 27 to legalize same-sex marriage, seven days ahead of the two-year deadline issued by the country\'s Constitutional Court in 2017. This would make Taiwan the first country in Asia to legally recognize unions between same-sex couples. The law is to take effect late this week.\\nThe Legislative Yuan debated three competing bills, and selected the one posed by the country\'s cabinet, which used the word \\"marriage,\\" over the two posed by conservatives, which used the terms \\"same-sex family relationship\\" and \\"same-sex union.\\" The selected bill does not offer same-sex couples all the same rights as their heterosexual counterparts; there are limits on adoption rights and marriage with foreigners.\\nJennifer Lu of Marriage Equality Coalition Taiwan said, \\"[I]t\'s still not full marriage rights; we still need to fight for co-adoption rights, and we are not sure about foreigner and Taiwanese marriage, and also gender equality education.\\"\\nThe Taiwanese government held a referendum in November 2018, allowing the population to vote on same-sex marriage, and 67% came out against.\\nXiaogang Wei of the Beijing Gender Health Education Institute commented on the Legislative Yuan\'s decision: \\"The Chinese government has pointed to cultural tradition as a reason for same-sex marriage being unsuitable in China. But the decision in Taiwan, which shares a cultural tradition with us, proves that Chinese culture can be open, diverse and progressive.\\"\\nIn mainland China, which claims sovereignty over Taiwan, homosexuality is technically not illegal, but late last year a same-sex erotica author was sentenced to ten years in prison, and same-sex marriage is not recognized.\\nIn 2017, Taiwan\'s Constitutional Court, which rules on constitutional matters, said not allowing gay citizens to marry constituted \\"different treatment\\" incompatible with the constitution. The decision prompted objections from conservatives opposing recognition of gay marriage.","domain":"","date":"","authors":"","title":"","target":"discrimination"}' --output response.txt

'''