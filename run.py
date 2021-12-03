from src.main.config import create_app
from src.main.config import config
import os

if __name__ == '__main__':
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(config[env])
