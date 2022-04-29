from decimal import Decimal
from math import prod

from MCompany.models import Event, Service


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    
    Note in session key, there are key-value pairs. So
    You can try this:
    py manage.py shell
    from django.contrib.sessions.models import Session
    s= Session.objects.get(pk='2uyjd58ac565llkud7gr99lvgs5tr30u')
    s.get_decoded()
    
    Note: 1l7d8zc4bobr56kz4ui8ag6xpt39imuqis a value of sesssion id(you can get it by inspecting in browser)
    It returns dictionary with user_id key-value pair.That's why we can directly visit the page after first time when loginto site
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        
        #If there is no session id set a new one. basket should be set since if statement fails we get unknown arg
        if 'skey' not in self.session:
            basket = self.session['skey'] = {} 
            
        self.basket = basket
        print('\nAt Initialization, Basket Session Products:',self.basket)

        
    """
    Adding and updating the users basket session data
    """
    def add(self, product, product_type, ordered_by, sits):
        product_name = str(product.name) #get the product id
        total_price= product.price *sits
        if product_type=='service':
            if product_name not in self.basket:
                print(f'Adding product of type {product_type}.')
                self.basket[product.name] = { 'id':product.id,
                                              'price': str(product.price),
                                               'type': product_type,
                                               'ordered_by':ordered_by,
                                               'sits':sits,
                                               'totalprice': str(total_price)
                                              #'product':Service.objects.filter(id=product.id, name=product.name).first()
                                        } #create
            else:
                print(f'Product {product_name} already added!')

        if product_type=='event':
            if product_name not in self.basket:
                print(f'Adding product of type {product_type}.')
                self.basket[product.name] = { 'id':product.id,
                                              'price': str(product.price),
                                              'type': product_type,
                                                'ordered_by':ordered_by,
                                                'sits':sits,
                                                'totalprice': str(total_price)
                                        } #create
            else:
                print(f'Product {product_name} already added!')
        self.save()


    """
    Collect the product_id in the session data
    Append extra key: product and 'total_price' to basket dictionary
    
    Return products  for cart items while looping
    Used in CONTEXT_PROCESSORS
    """
    def __iter__(self):
        print('keys:',self.basket.keys())
        product_keys = self.basket.keys()
        for productkey in product_keys:
            if self.basket[productkey]['type']=='service':
              service_obj = Service.objects.get(id=self.basket[productkey]['id'])
              print(service_obj)
              self.basket[productkey]['product'] = service_obj
  
            if self.basket[productkey]['type']=='event':
              event_obj = Event.objects.get(id=self.basket[productkey]['id'])
              print(event_obj)
              self.basket[productkey]['product'] = event_obj
        print('\nIter:',self.basket)   
        for item in self.basket.values():
            yield item
            
         
    """
    Get the basket data and count the qty of items
    self.basket.values()
    {'price': '23.00'},
    {'qty': 1}}
    """ 


    def get_cart_items(self):
        count=0;
        for i in self.basket:
            print('key:',i)
            count=count+1
        return count
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['sits'] for item in self.basket.values())


    def delete(self, product_id):
        """
        Delete item from session data
        """
        product_id = str(product_id)

        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session['skey']
        #del self.session["address"]
       # del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True
