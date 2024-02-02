from django.urls import path
from .views import (
    HostelView,
    RoomEditView,
    RoomAddView,
    RoomDeleteView,
    SportListView,
    SportEditView,
    SportAddView,
    SportDeleteView,
    TransportListView,
    TransportEditView,
    TransportAddView,
    TransportDeleteView,
)

app_name = 'MOthers'  

urlpatterns = [

    path('hostel', HostelView.as_view(), name='hostel-view'),
    path('room/edit', RoomEditView.as_view(), name='room-edit-view'),
    path('room/add', RoomAddView.as_view(), name='room-add-view'),
    path('room/delete', RoomDeleteView.as_view(), name='room-delete-view'),

    # Sport URLs
    path('sports', SportListView.as_view(), name='sport-list-view'),
    path('sports/edit', SportEditView.as_view(), name='sport-edit-view'),
    path('sports/add', SportAddView.as_view(), name='sport-add-view'),
    path('sports/delete', SportDeleteView.as_view(), name='sport-delete-view'),

    # Transport URLs
    path('transport', TransportListView.as_view(), name='transport-list-view'),
    path('transport/edit', TransportEditView.as_view(), name='transport-edit-view'),
    path('transport/add', TransportAddView.as_view(), name='transport-add-view'),
    path('transport/delete', TransportDeleteView.as_view(), name='transport-delete-view'),
]
