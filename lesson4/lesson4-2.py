"""
Please change ownership for all issues in bugs.json to 'qa5'.
Save result to bugs_new.json. Use json loads and dumps methods.
"""

import json
import StringIO

with open('bugs.json', 'r') as jsn:
    jsn = json.loads(jsn.read())
    
    for i in jsn:
        i["Owner"] = 'qa5'

    new_file = open('bugs_new.json','w')
    new_file.write(json.dumps(jsn, sort_keys=True, indent=4))
    new_file.close()
