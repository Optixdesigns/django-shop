from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from articles.models import Article

class ArticleInline(admin.StackedInline):
  model = Article
  extra = 0
  fieldsets = (
      (None, {
          "fields": ["title", "slug", "status", "publish_date", "expiry_date", "body",],
      }),
  )

  verbose_name = "Sub Article"
  verbose_name_plural = "Sub Articles"

class ArticleAdmin(NodeAdmin):
	extra_fieldsets = ((None, {"fields": ("image", "body",)}),)
	inlines = [
    	ArticleInline,
  ]
	pass

admin.site.register(Article, ArticleAdmin)