from flask import Blueprint, request, make_response, jsonify
from ...extensions.database import db
from ...models.media import Media


bp = Blueprint("medias", __name__, url_prefix="/medias")

@bp.route('/', methods=['GET', 'POST'])
def medias():
    if request.method == 'GET':
        query_string_params = request.args
        include_deleted = query_string_params.get('include_deleted') == "true"

        if include_deleted:
            medias = Media.query.all()
        else:
            medias = Media.query.filter_by(deleted=False).all()
        result = jsonify(medias)

        response = make_response(result, 200)

        return response
    
    elif request.method == 'POST':
        return 'Insert media'


@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def media(id):
    if request.method == 'GET':
        return 'Get media with id {}'.format(id)

    elif request.method == 'PUT':
        return 'Update media with id {}'.format(id)

    elif request.method == 'DELETE':
        return 'Delete media with id {}'.format(id)
