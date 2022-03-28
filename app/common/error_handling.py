from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError


def register_error_handlers(app: Flask):
    # @app.errorhandler(Exception)
    # def handle_exception_error(e):
    #     if isinstance(e, ValidationError):
    #         return jsonify(e.messages), 400
    #     return jsonify({'msg': 'Internal server error'}), 500
    # @app.errorhandler(405)
    # def handle_405_error(e):
    #     return jsonify({'msg': 'Method not allowed'}), 405
    # @app.errorhandler(403)
    # def handle_403_error(e):
    #     return jsonify({'msg': 'Forbidden error'}), 403
    # @app.errorhandler(404)
    # def handle_404_error(e):
    #     return jsonify({'msg': 'Not Found error'}), 404
    # # @app.errorhandler(AppErrorBaseClass)
    # # def handle_app_base_error(e):
    # #     return jsonify({'msg': str(e)}), 500
    # # @app.errorhandler(ObjectNotFound)
    # # def handle_object_not_found_error(e):
    # #     return jsonify({'msg': str(e)}), 404
    pass