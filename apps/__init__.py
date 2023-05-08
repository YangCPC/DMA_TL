from flask import Flask

import settings
from apps.apis.CE_apis import CE_bp
from apps.apis.MH_apis import MH_bp

from exts import db, cache, cors

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379
}

def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    # db initialization
    db.init_app(app=app)
    # cache initialization
    cache.init_app(app=app, config=config)
    # cors initizalation
    cors.init_app(app=app, supports_credentials=True)
    # register blueprint
    app.register_blueprint(MH_bp)
    app.register_blueprint(CE_bp)

    return app