import os


basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'wdefrgthnmjghfytdreasdvbgmuyjthrgdxfhmuyjrhtgfyou-will-never-guess-this-key-1234-5678-91011-1213-1415'

MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 1gb max upload size
