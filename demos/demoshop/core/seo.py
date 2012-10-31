from rollyourown import seo
from django.conf import settings

def default_title(metadata, model_instance=None, **kwargs):
  if hasattr(model_instance, 'title'):
    return model_instance.title
  elif hasattr(model_instance, 'name'):
    return model_instance.name
  
  return getattr(settings, 'SITE_NAME', '')

def default_description(metadata, model_instance=None, **kwargs):
  if hasattr(model_instance, 'intro'):
    return model_instance.intro

  return getattr(settings, 'SITE_DESCRIPTION', '')

def default_keywords(metadata, model_instance=None, **kwargs):
  if hasattr(model_instance, 'tags'):
    return ",".join([tag.name for tag in model_instance.tags.all()])
  
  return getattr(settings, 'SITE_KEYWORDS', '')

class SiteMetadata(seo.Metadata):
  #title       = seo.Tag(head=True, max_length=68, populate_from=default_title, help_text="If empty uses the content of the title field. Si?")
  description = seo.MetaTag(max_length=200, populate_from=default_description, help_text="If empty uses the content of the intro field. Si?")
  keywords    = seo.KeywordTag(populate_from=default_keywords, help_text="If empty uses the content of the Tags field. Si?")

  class Meta:
    seo_models = ('articles.Article',)
    verbose_name = "Meta Data"
    verbose_name_plural = "Meta Data"