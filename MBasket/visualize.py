'''

from urllib import request

basket.session = request.session

session = {'basket': <MBasket.basket.Basket object at 0x04853E50>}= 
{   
    'skey': {
            'service1': {'id': 1, 'price': '23.00', 'type': 'service'}, 
            'event1': {'id': 1, 'price': '34.00', 'type': 'event'}
        }, 
    '_auth_user_id': '1',
    '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend', 
    '_auth_user_hash': '2290aa90789153435ce072579540d6deddb1ad3afd3cbdad18632a5b0ce2c28c'
 }



#At initalization
basket= self.session.get('skey')= {
'8': {
    'id': 1
    'price': '33.00',
    'type':'event'
    },

'9': {
    'id':4,
    'price': '23.00',
    'type':'service
    }
}

#when we loop the basket the basket will changed as def **iter**(self) is called
iter=self.session.get('skey')=[
{
'price': Decimal('23.00'),
'qty': 1,
'product': '<Product: Female Summer Shirt Pants>',
'total_price': Decimal('23.00')
},

        {
            'price': Decimal('33.00'),
            'qty': 1,
            'product': '<Product: Esprit Ruffle ShirtPant Pairs>',
            'total_price': Decimal('33.00')
        },

]

[{
'price': '33.00',
'qty': 1,
'title': 'Esprit Ruffle ShirtPant Pairs',
'thumbnail': 'https://res.cloudinary.com/dcgrv6shk/image/upload/v1648044862/VanezStore/product1_gypgoa.jpg'},

    {'price': '23.00',
    'qty': 2,
    'title': 'Esprit Ruffle ShirtPant Pairs',
     'thumbnail': 'https://res.cloudinary.com/dcgrv6shk/image/upload/v1648044862/VanezStore/product1_gypgoa.jpg'},

     {'price': '33.00',
      'qty': 1,
       'title': 'Esprit Ruffle ShirtPant Pairs',
       'thumbnail': 'https://res.cloudinary.com/dcgrv6shk/image/upload/v1648044862/VanezStore/product1_gypgoa.jpg'}

]

{'8': {'price': '33.00', 'qty': 1, 'title': 'Esprit Ruffle ShirtPant Pairs', 'thumbnail': 'https://res.cloudinary.com/dcgrv6shk/image/upload/v1648044862/VanezStore/product1_gypgoa.jpg'}, '9': {'price': '23.00', 'qty': 2, 'title': 'Esprit Ruffle ShirtPant Pairs', 'thumbnail': 'https://res.cloudinary.com/dcgrv6shk/image/upload/v1648044862/VanezStore/product1_gypgoa.jpg'}}


'''
