import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe6Wa\xf6\xbd\xa0\\\x8c\x88k\x86"\x9ai\x92\x80'

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment'}
