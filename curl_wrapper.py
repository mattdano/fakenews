import json
import gzip
import os

# insert the test json into this script.
#article_text = '''On Friday the legislature of Taiwan, the Legislative Yuan, voted 66 to 27 to legalize same-sex marriage, seven days ahead of the two-year deadline issued by the country\'s Constitutional Court in 2017. This would make Taiwan the first country in Asia to legally recognize unions between same-sex couples. The law is to take effect late this week.\nThe Legislative Yuan debated three competing bills, and selected the one posed by the country\'s cabinet, which used the word \"marriage,\" over the two posed by conservatives, which used the terms \"same-sex family relationship\" and \"same-sex union.\" The selected bill does not offer same-sex couples all the same rights as their heterosexual counterparts; there are limits on adoption rights and marriage with foreigners.\nJennifer Lu of Marriage Equality Coalition Taiwan said, \"[I]t\'s still not full marriage rights; we still need to fight for co-adoption rights, and we are not sure about foreigner and Taiwanese marriage, and also gender equality education.\"\nThe Taiwanese government held a referendum in November 2018, allowing the population to vote on same-sex marriage, and 67% came out against.\nXiaogang Wei of the Beijing Gender Health Education Institute commented on the Legislative Yuan\'s decision: \"The Chinese government has pointed to cultural tradition as a reason for same-sex marriage being unsuitable in China. But the decision in Taiwan, which shares a cultural tradition with us, proves that Chinese culture can be open, diverse and progressive.\"\nIn mainland China, which claims sovereignty over Taiwan, homosexuality is technically not illegal, but late last year a same-sex erotica author was sentenced to ten years in prison, and same-sex marriage is not recognized.\nIn 2017, Taiwan\'s Constitutional Court, which rules on constitutional matters, said not allowing gay citizens to marry constituted \"different treatment\" incompatible with the constitution. The decision prompted objections from conservatives opposing recognition of gay marriage.'''
article_text =  '''WASHINGTON — The House voted to impeach President Donald Trump Wednesday after releasing hundreds of pages of text messages that point to clear evidence of obstruction of justice and communication with the head of the Trump Organization about a potential business deal in Russia. The 220-197 vote came after weeks of debate over whether new evidence released by special counsel Robert Mueller’s office signaled sufficient grounds for Trump’s removal from office. The president personally denounced the move, announcing his intent to veto the resolution and accusing Democrats of plotting to remove him from office through a “con job.”\n“This is all a big con job,” he said during an appearance in Texas. “They got caught.”\nA number of Democratic lawmakers went further, calling for Trump’s impeachment on the grounds that he obstructed justice. Democrats hold the House majority, and if the Senate fails to convict Trump, the president can be removed from office by a two-thirds vote.\nBut even with Trump’s political allies organizing from the White House, Republicans in the House stood united behind their leader, noting the historical difficulty of making the case for impeachment. “This is not a decision for the president,” said House Speaker Paul Ryan, R-Wis. “It’s not one for this body, and I think it’s a dereliction of duty for the minority party to be making these calls.”\nDemocrats on the House Judiciary Committee on Tuesday said they were not bound by Ryan’s defense. They released an 11-page joint report with Republicans on the House Oversight and Government Reform Committee that took a different tack, emphasizing that Mueller had not decided whether the case warranted impeachment. Rep. Jerrold Nadler, D-N.Y., the committee’s chairman, told reporters before the vote that he hoped the two reports would “send a clear message to the president that we in this body are not going to stand for obstruction of justice.” But when asked whether the report would build the case for impeachment, he said: “What’s far more likely to build a case for impeachment are the indictments and evidence produced through the special counsel’s work.”\nOn Tuesday night, the White House issued a statement proclaiming that the book by a former FBI deputy director, which has been cited by Democrats in support of impeachment, had been “made up and defamatory” to the president.\nThat statement drew swift and heavy rebukes from a number of Democrats, who said they had found the statement “beyond astonishing.”\nThe Democratic report, citing redacted text messages sent by former FBI counterintelligence agent Peter Strzok, revealed what the party called “a pattern of bias” and “an affinity for the Russian regime.”\nThe report did not include a full, uncensored text message Strzok sent to a friend after Trump was elected that said: “I’ll stop it.” That led Democrats to bemoan the language used, questioning what is or is not in the special counsel’s investigative file.\nThe report also quoted a review of emails and witness testimony to Mueller that said Trump “has obstructed justice in the Russia investigation” by firing FBI Director James Comey, by urging Attorney General Jeff Sessions to recuse himself from the Russia investigation and by urging his son, Donald Trump Jr., to meet with a Kremlin-connected Russian lawyer at Trump Tower in 2016.\n“This has never happened in the history of our country,” Nadler said of the president. “No president has ever tried to interfere with an investigation into his own conduct.”\nThe vote was also led by Democrats who have been outspoken against Trump, including Rep. Al Green, D-Texas, who took out  newspaper ads calling for the president’s impeachment. Rep. Maxine Waters, D-Calif., another outspoken Trump critic, said Trump’s ties to Russia were “becoming more and more ominous,” and said “as we go on, we are going to see if we can’t get the articles of impeachment out.”\nRep. Tony Cárdenas, D-Calif., a member of the Judiciary Committee, said many Democrats would be eager to see whether the newly discovered evidence could be used to support impeachment. “I think it will be the nail in the coffin of the ‘non-con,’” he said.'''

test_str = '{"article":"%s","domain":"","date":"","authors":"","title":"","target":"discrimination"}'%article_text
print(len(test_str))
size = len(test_str)

outfile = '''curl 'https://discriminate.grover.allenai.org/api/disc' \\
-XPOST \\
-H 'Accept: application/json, text/plain, */*' \\
-H 'Content-Type: application/json;charset=utf-8' \\
-H 'Origin: https://grover.allenai.org' \\
-H 'Content-Length: %d' \\
-H 'Accept-Language: en-gb' \\
-H 'Host: discriminate.grover.allenai.org' \\
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15' \\
-H 'Referer: https://grover.allenai.org/detect' \\
-H 'Accept-Encoding: gzip, deflate, br' \\
-H 'Connection: keep-alive' \\
--data $'{"article":"%s","domain":"","date":"","authors":"","title":"","target":"discrimination"}' \\
--output n_response.txt.gz'''%(size,article_text)
print(outfile)

f = open('./new_curler.sh','w')
f.write(outfile)
f.close()

exit()
os.system('chmod 777 ./new_curler.sh')
os.system('./new_curler.sh')

print('all done')

exit()


f = gzip.open('./response.txt.gz', 'rb')
file_content = f.read()
f.close()


results_json = json.loads((file_content))

print(float(results_json['groverprob']))