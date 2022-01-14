import environ
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)

environ.Env.read_env(env_file=BASE_DIR.resolve().as_posix() + '/.env')

DEBUG = env.get_value('DEBUG')
SECRET_KEY = env.get_value('SECRET_KEY')
ALLOWED_HOSTS = env.get_value('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env.get_value('DB_NAME'),
        'USER': env.get_value('DB_USER'),
        'PASSWORD': env.get_value('DB_PASSWORD'),
        'HOST': env.get_value('DB_HOST'),
        'PORT': env.get_value('DB_PORT'),
    }
}
