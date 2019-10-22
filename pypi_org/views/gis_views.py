import flask

from final.pypi_org.infrastructure.view_modifiers import response
import final.pypi_org.services.gis_service as gis_service

blueprint = flask.Blueprint('gis', __name__, template_folder='templates')

@blueprint.route('/gis')
@response(template_file='gis/page.html')
def about():
    return {}

# @blueprint.route('/gis')
# @response(template_file='gis/page.html')
# def gis_page():
#     # print("Getting GIS page for {}".format(full_url))
#
#     page = gis_service.get_page('gis/page.html')
#     if not page:
#         return flask.abort(404)
#
#     return page
