import toml
config = toml.load('config.toml')


if __name__ == "__main__":
    
    import json
    print(json.dumps(config, indent=4))