import app
from settings import DURATION


if __name__ == "__main__":
    
    env = app.create_env()
    env.run(until=DURATION)