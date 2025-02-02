from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(BlogPost, BlogPostTranslationOptions)
