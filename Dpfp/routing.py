'''
-----------------------------------------------
DJANGO PRO STARTER TEMPLATE: CHANNELS ROUTING
-----------------------------------------------

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import app1  #your custom  app
import app2
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
             app1.routing.websocket_patterns,
             app2.routing.websocket_patterns,
        )
    )
})
'''
