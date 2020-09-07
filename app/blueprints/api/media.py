from flask import Blueprint, request


bp = Blueprint("medias", __name__, url_prefix="/medias")

@bp.route('/', methods=['GET', 'POST'])
def medias():
    if request.method == 'GET':
        return 'Get all media'
    
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
