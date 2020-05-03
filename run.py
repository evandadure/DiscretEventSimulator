import app

from settings import config



if __name__ == "__main__":
    
    env = app.init_env()
    env.run(until=config['simulation']['duration'])

    app.printResults()
