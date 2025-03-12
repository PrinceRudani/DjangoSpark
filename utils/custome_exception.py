from django.shortcuts import render
from custom_enum.http_enum import HttpStatusCodeEnum, ResponseMessageEnum  # Import
# your enums
import logging
import sys
from django.db.utils import IntegrityError

logger = logging.getLogger("FlaskMVCProject")  # Ensure your logger is set up

class AppServices:
    @staticmethod
    def app_response(status_code: int, message: str, success: bool = None, data: any = None) -> dict:
        response = {
            "status_code": status_code,
            "success": success,
            "message": message,
            "data": data
        }
        return response

    @staticmethod
    def handle_exception(exception, is_raise=False):
        exc_type, _, tb = sys.exc_info()
        f = tb.tb_frame
        line_no, filename, function_name = \
            tb.tb_lineno, f.f_code.co_filename, f.f_code.co_name

        # Log the detailed exception for debugging purposes
        message = exception.detail if hasattr(exception, "detail") and bool(
            exception.detail) \
            else f"Exception type: {exc_type}, " \
                 f"Exception message: {exception.__str__()}, " \
                 f"Filename: {filename}, " \
                 f"Function name: {function_name} " \
                 f"Line number: {line_no}"

        logger.error(f"Exception error message: {message}")

        # If it's an IntegrityError (duplicate entry), return a user-friendly message
        if isinstance(exception, IntegrityError):
            user_message = "A category with this name already exists. Please choose a different name."
        else:
            user_message = ResponseMessageEnum.INTERNAL_SERVER_ERROR.value  #
            # Default error message

        if is_raise:
            # Render custom error page when is_raise is True
            return render(None, "error/custom_error_page.html", {
                "message": user_message,
                "status_code": HttpStatusCodeEnum.INTERNAL_SERVER_ERROR.value
            })

        # If not is_raise, render error page with details
        return render(None, "error/custom_error_page.html", {
            "message": user_message,  # Provide a user-friendly error message
            "status_code": HttpStatusCodeEnum.INTERNAL_SERVER_ERROR.value
        })
