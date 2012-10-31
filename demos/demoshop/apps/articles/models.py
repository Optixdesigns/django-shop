from django.db import models
from django.contrib.auth.models import User
from datetime import *

from hub.node.models import Node
from hub.core.models import Featurable, RichText
from sorl.thumbnail import ImageField

class Article(Node, Featurable, RichText):
	image = ImageField(upload_to='article/', blank=True, null=True, default='project/images/no-image.jpg')
	pass