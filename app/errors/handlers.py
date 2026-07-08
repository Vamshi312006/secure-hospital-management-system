from flask import (
    flash,
    redirect,
    request,
)

from app.rules.base import BusinessRuleError
from app.validators.base import ValidationError


def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def validation_error(error):

        flash(str(error), "danger")

        return redirect(
            request.referrer or "/"
        ), 400


    @app.errorhandler(BusinessRuleError)
    def business_error(error):

        flash(str(error), "danger")

        return redirect(
            request.referrer or "/"
        ), 400
