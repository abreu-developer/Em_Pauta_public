
from cerberus import Validator


def insert_movie_validator(body: dict) -> None:
    body_validator = Validator({
        "data": {
            "type": "dict",
            "required": True,
            "schema": {
                "name": {"type": "string", "required": True},
                "genre": {"type": "string", "required": True},
                "director": {"type": "string", "required": True},
                "release_date": {"type": "string", "required": True},
                "duration": {"type": "integer", "required": True},
                "review": {"type": "string", "required": True},
                "score": {"type": "integer", "required": True},
                "poster_url": {"type": "string", "required": True},
                "comments": {
                    "type": "list",
                    "required": True,
                    "schema": {"type": "dict"},
                },
            },
        }
    })
    

    response = body_validator.validate(body)
    
    if response is False:
        raise Exception(body_validator.errors)
