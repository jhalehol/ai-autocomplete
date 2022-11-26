from fastapi import APIRouter, HTTPException
import logging

import autocomplete_api.context as context
from autocomplete_api.exception.configuration_exception import ConfigurationException
from autocomplete_api.exception.forbidden_exception import ForbiddenException 

router = APIRouter(
    prefix = "/suggest",
    tags = ["suggestions"],
    responses = {
        "500": { "description": "Configuration issue" },
        "403": { "description": "Operation not allowed" },
        })

__LOGGER = logging.getLogger(__name__)


@router.get("/")
def get_suggestions(prefix: str, limit: int = None):
    try:
        result: list = context.search_service.search(prefix, limit)
        return result
    except ConfigurationException as ex:
        __LOGGER.error('Configuration issue found %s', ex.message)
        raise HTTPException(status_code=500, detail='Server configuration error')
    except ForbiddenException as ex:
        raise HTTPException(status_code=403, detail=ex.message)
    