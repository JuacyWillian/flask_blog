import os
import sys


BASEDIR = os.path.abspath(os.path.dirname(__file__))

# DATABASE
DATABASE = {
    'sqlite': 'sqlite:///'+os.path.join(BASEDIR, 'database', 'storage.db'),
    'mysql': '',
    'postgres': '',
}

SQLALCHEMY_DATABASE_URI = DATABASE['sqlite']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SECURITY
SECRET_KEY = 'a vingança nunca é plena, mata a alma e a envenena!'
ENABLE_CSRF = True

# Debug Toolbar Config
DEBUG_TB_ENABLED = True
DEBUG_TB_INTERCEPT_REDIRECTS = False