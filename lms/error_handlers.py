# from flask import render_template, current_app

# def register_error_handlers(app):

#     @app.errorhandler(500)
#     def internal_server_error(error):
#         current_app.logger.error(f'Internal Server Error: {error}', exc_info=True)
#         return render_template('500.html'), 500
