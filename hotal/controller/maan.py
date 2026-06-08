from odoo import http
from odoo.http import request
import requests
import logging

_logger = logging.getLogger(__name__)
TOKEN = "1572b9bd7cadceec198e91b0af65c60309b6664f70bcf074d7e50688baefab49"
API_URL = "https://gorest.co.in/public/v2"
class Hospitall(http.Controller):
    @http.route('/users', type='http', auth='public', website=True)
    def users_page(self, **kwargs):
        TOKEN = "1572b9bd7cadceec198e91b0af65c60309b6664f70bcf074d7e50688baefab49"
        try:
            response = requests.get(
            'https://gorest.co.in/public/v2/users',
            headers={'Authorization': f'Bearer {TOKEN}'}
                )
            all_users = response.json()
            users = [all_users[0]] if all_users else []
        except Exception as e:
            _logger.error("Error: %s", str(e))
            users = []

        return request.render('hotal.users_page', {
        'users': users
    })

    @http.route('/users/edit/<int:user_id>', type='http', auth='public', website=True)
    def edit_user_page(self, user_id, **kwargs):
        try:
            response = requests.get(f'{API_URL}/users/{user_id}',headers={'Authorization': f'Bearer {TOKEN}'},timeout=10)
            #_logger.info("Status: %s", response.status_code)
            #_logger.info("User data: %s", response.text)
            user = response.json()
        except Exception as e:
            _logger.error("Error: %s", str(e))
            user = {}
            logger.info("Rendering edit page for user: %s", user)
        return request.render('hotal.edit_user_page', {'user': user})

    # ===== حفظ التعديل =====
    
    @http.route('/users/update/<int:user_id>',
            type='http',
            auth='public',
            website=True,
            methods=['POST'],
            csrf=True)
    def update_user(self, user_id, **post):

        try:
            _logger.info("USER ID = %s", user_id)
            _logger.info("POST = %s", post)

            response = requests.patch(
            f'{API_URL}/users/{user_id}',
            headers={
                'Authorization': f'Bearer {TOKEN}',
                'Content-Type': 'application/json'
            },
            json={
                'name': post.get('name'),
                'email': post.get('email'),
                'gender': post.get('gender'),
                'status': post.get('status'),
            },
            timeout=10)

            _logger.info("STATUS = %s", response.status_code)
            _logger.info("BODY = %s", response.text)

            return request.redirect('/users')

        except Exception as e:
            return f"ERROR: {str(e)}" 