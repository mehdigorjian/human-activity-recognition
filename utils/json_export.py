import json
import numpy as np
class DataEncoder(json.JSONEncoder):
    def default(self, o):
        if (isinstance(o, float)
            or isinstance(o, np.float32)
            or isinstance(o, int)):
            return str(o)
        return json.JSONEncoder.default(self, o)

# writing json file as: timeLabel.json
def to_json_file(dict_key, list_input):
	if not isinstance(dict_key, str):
		dict_key = str(dict_key)
	if not isinstance(list_input, list):
		list_input = list(list_input)
	jFile = {}
	jFile[dict_key] = list_input
	print(jFile)
	with open('timeLable.json', 'w+') as j:
		json.dump(jFile, j, cls=DataEncoder)