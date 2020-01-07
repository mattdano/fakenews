import json
import gzip

f = gzip.open('./response.txt.gz', 'rb')
file_content = f.read()
f.close()


results_json = json.loads((file_content))

print(float(results_json['groverprob']))

