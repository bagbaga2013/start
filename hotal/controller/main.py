from odoo import http
from odoo.http import request
import requests
class Hospital(http.Controller):

    # Sample Controller Created
    @http.route('/hospital/patient/',type='http', auth='public', website=True)
    def hospital_patient(self, **kwargs):
        #return "Thanks for watching"
        return request.render("hotal.patients_page1", {})


    # controllers/main.py


    @http.route('/patients', type='http', auth='public', website=True)
    def patients_page(self, **kwargs):
        try:
            response = requests.get('https://gorest.co.in/public/v2/users')
            patients = response.json()
        except Exception:
            patients = []

        return request.render('hotal.patients_page', {
            'patients': patients
        })    
    
    ################################################################################

    # controllers/main.py


API_URL = "https://gorest.co.in/public/v2/users"

class HotalController(http.Controller):

    # ===== عرض المستخدمين =====
    @http.route('/users', type='http', auth='public', website=True)
    def users_page(self, **kwargs):
        try:
            response = requests.get(f'{API_URL}/users')
            users = response.json()
        except Exception:
            users = []

        return request.render('hotal.users_page', {
            'users': users
        })

    # ===== تعديل مستخدم =====
    @http.route('/users/edit/<int:user_id>', type='http', 
                auth='public', website=True)
    def edit_user_page(self, user_id, **kwargs):
        try:
            response = requests.get(f'{API_URL}/users/{user_id}')
            user = response.json()
        except Exception:
            user = {}

        return request.render('hotal.edit_user_page', {
            'user': user
        })

    # ===== حفظ التعديل =====
    @http.route('/users/update/<int:user_id>', type='http',
                auth='public', website=True, methods=['POST'], csrf=True)
    def update_user(self, user_id, **post):
        TOKEN = "YOUR_GOREST_TOKEN"  # ضع التوكن هنا
        try:
            requests.patch(
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
                }
            )
        except Exception:
            pass

        return request.redirect('/users')