from django.urls import path
from . import views

api_list = [
    {
        'name': 'AI Agent',
        'url': 'ai-agent',
        'description': 'AI Agent'
    }
]

urlpatterns = [
    path('', views.index, name='calling apis'),
    # <str:api_name> covert api_name to string
    # <int:api_id> covert api_id to integer (This have to set before <str:api_name>)
    path('<int:api_id>', views.call_api_by_number, name='calling apis by number'),
    path('<str:api_name>', views.call_api_by_name, name='calling apis by name'),
]
