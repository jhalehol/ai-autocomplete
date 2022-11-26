from fastapi import APIRouter, HTTPException
import logging

import context as context
from exception.configuration_exception import ConfigurationException
from exception.forbidden_exception import ForbiddenException 

tags_metadata = [
    {
        "name": "suggestions",
        "description": "Generates suggestions for autocomplete operations with prefix data",
    },
]

router = APIRouter(
    prefix = "/suggest",
    tags = ["suggestions"],
    responses = {
        "500": { "description": "Configuration issue" },
        "403": { "description": "Operation not allowed" },
        })

__LOGGER = logging.getLogger(__name__)


@router.get("/", summary="Return an array of suggestions given the prefix, if limit is not provided will use as limit the default configuration")
def get_suggestions(prefix: str, limit: int = None):
    try:
        result: list = context.search_service.search(prefix, limit)
        return result
    except ConfigurationException as ex:
        __LOGGER.error('Configuration issue found %s', ex.message)
        raise HTTPException(status_code=500, detail='Server configuration error')
    except ForbiddenException as ex:
        raise HTTPException(status_code=403, detail=ex.message)
    