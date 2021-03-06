from flask import Blueprint, request, make_response, jsonify, Response
from sqlalchemy.exc import IntegrityError
from datetime import datetime, date
from ...extensions.database import db
from ...models.media import Media
from ...helper import (check_required_parameters, error_message,
    validate_date_format, format_upload_date)


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
            return error_message("No valid informed data.")
        
        try:
            check_required_parameters(data)
            validate_date_format(data.get('upload_date'))
        except KeyError as e:
            arg = e.args[0].get('arg')
            return error_message("Required field '{}' is null or invalid.".format(arg))
            
        except ValueError:
            return error_message("Invalid date format. Expected YYYY-mm-dd string format.")

        try:
            data['upload_date'] = format_upload_date(data.get('upload_date'))
            new_media = Media(**data)
            db.session.add(new_media)
            db.session.commit()

            response = make_response({'id': new_media.id}, 201)

        except IntegrityError:
            return error_message("There already has a media with the informed url.")

        except BaseException as e:
            return error_message(e)

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
        media = Media.query.get(id)

        if media is not None:
            data = request.json

            for key in data.keys():
                if key == 'upload_date':
                    validate_date_format(data[key])
                    data[key] = format_upload_date(data[key])
                setattr(media, key, data[key])

            db.session.add(media)
            db.session.commit()

            response = Response(status=204)
            response.headers['Content-Type'] = 'application/json'
        else:
            response = Response(status=404)
            response.headers['Content-Type'] = 'application/json'

        return response


    elif request.method == 'DELETE':
        media = Media.query.get(id)

        if media is not None:    
            media.deleted = True
            db.session.add(media)
            db.session.commit()
    
            response = Response(status=200)
            response.headers['Content-Type'] = 'application/json'
        else:
            response = Response(status=404)
            response.headers['Content-Type'] = 'application/json'

        return response
