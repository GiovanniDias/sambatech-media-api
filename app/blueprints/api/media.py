from flask import Blueprint, request, make_response, jsonify, Response
from sqlalchemy.exc import IntegrityError
from datetime import datetime, date
from ...extensions.database import db
from ...models.media import Media
from ...helper import check_required_parameters


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
        try:
            data = request.json
        except BaseException:
            message = "No valid informed data."
            response = make_response(message, 400)
            return response
        
        try:
            check_required_parameters(data)
        except KeyError as e:
            arg = e.args[0].get('arg')
            message = "Required field '{}' is null or invalid.".format(arg)
            response = make_response(message, 400)
            return response
        except ValueError:
            message = "Invalid date format. Expected YYYY-mm-dd string format."
            response = make_response(message, 400)
            return response

        try:
            upload_date = data['upload_date']
            dt = datetime.strptime(upload_date, "%Y-%m-%d")
            data['upload_date'] = date(dt.year,dt.month,dt.day)

            new_media = Media(**data)
            db.session.add(new_media)
            db.session.commit()
            
            response = make_response({'id': new_media.id}, 200)

        except IntegrityError:
            message = "There already has a media with the informed url."
            response = make_response(message, 400)
            return response

        except BaseException:
            response = Response(status=400)
            response.headers['Content-Type'] = 'application/json'

        return response


@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def media(id):
    if request.method == 'GET':
        media = Media.query.get(id)
        result = jsonify(media)

        if media is not None:
            response = make_response(result, 200)
        else:
            response = Response(status=404)
            response.headers['Content-Type'] = 'application/json'

        return response

    elif request.method == 'PUT':
        return 'Update media with id {}'.format(id)

    elif request.method == 'DELETE':
        return 'Delete media with id {}'.format(id)
