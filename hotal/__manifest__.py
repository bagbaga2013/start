{
    'name': 'My Hotel',
    'version': '1.0',
    'depends': ['base','sale_management','mail'],
    'data': [
        'security/ir.model.access.csv', 
        'views/hotel_reservation_view.xml',
        'views/hotel_room_view.xml',
        'views/my_hotel_view.xml',
        'views/tag_view.xml',
        'views/my_hotel.xml',
        'views/templelet.xml',
        'views/templelet1.xml',
        'views/users_page.xml',
        'views/edit_user_page.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'hotal/static/src/css/property.css',
        ],
    },
    'application': True,
}
