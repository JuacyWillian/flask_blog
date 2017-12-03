from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_pyfile('config.py')

toolbar = DebugToolbarExtension(app)
Markdown(app)
bcrypt = Bcrypt(app)

assets = Environment(app)
assets.register('css', 'css/style.css', 'css/util.css', filters='cssmin', output='gen/main.css')
assets.register('js_all', 'js/script.js', filters='jsmin', output='gen/main.js')

assets.register('auth_style', 'css/auth.css', 'css/util.css', filters='cssmin', output='gen/auth.css', )
assets.register('auth_script', 'js/auth.js', filters='jsmin', output='gen/auth.js')

from .models import *

db.init_app(app)
migrate = Migrate(app, db)


@app.context_processor
def site_info():
    return dict(sitename='Juacy Willian')


from .views.core_bp import core
from .views.auth_bp import auth
from .views.admin_bp import admin

app.register_blueprint(core)
app.register_blueprint(auth)
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run(debug=True)
