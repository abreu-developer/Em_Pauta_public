from cerberus import Validator


def update_movie_validator(body: dict) -> None:
    body_validator = Validator({
        "data": {
            "type": "dict",
            "required": True,
            "schema": {
                "name": {"type": "string"},
                "genre": {"type": "string"},
                "director": {"type": "string"},
                "release_date": {"type": "string"},
                "duration": {"type": "integer"},
                "review": {"type": "string"},
                "score": {"type": "integer"},
                "poster_url": {"type": "string"},
                "comments": {
                    "type": "list",
                    "schema": {"type": "dict"},
                },
            },
        }
    })

    response = body_validator.validate(body)

    if response is False:
        raise Exception(body_validator.errors)
