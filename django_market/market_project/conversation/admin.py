from django.contrib import admin

from .models import Conversation, ConversationMassage

admin.site.register(Conversation)
admin.site.register(ConversationMassage)
