from fastapi import HTTPException
from loguru import logger

def internal_server_error(exc: Exception):
    logger.error(f"An error occurred: {exc}")
    logger.exception("Exception Stack Trace:")
    error_message = f"Internal server error: {exc}"
    return HTTPException(status_code=500, detail=error_message)