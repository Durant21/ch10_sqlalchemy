import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import final.pypi_org.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    # register_blueprints()
    # setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite')

    db_session.global_init(db_file)


def register_blueprints():
    from final.pypi_org.views import home_views
    from final.pypi_org.views import package_views
    from final.pypi_org.views import cms_views
    from final.pypi_org.views import gis_views

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(gis_views.blueprint)


register_blueprints()
setup_db()

if __name__ == '__main__':
    main()
