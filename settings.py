import toml
import json


config = toml.load('config.toml')
print(json.dumps(config, indent=4))


# environment
DURATION = config['environment']['duration']