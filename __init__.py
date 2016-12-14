from skygear.settings import settings
from skygear import static_assets
from skygear.utils.assets import relative_assets

from .chat import includeme

includeme(settings)

@static_assets(prefix='demo')
def chat_demo():
    return relative_assets('chat-SDK-JS/demo')
