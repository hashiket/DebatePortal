from django.contrib import admin
from .models import UsersType,DebateTopic,Views,Votes,DepateWinner,TopicSuggest
# Register your models here.
admin.site.register(UsersType)
admin.site.register(DepateWinner)
admin.site.register(DebateTopic)
admin.site.register(Views)
admin.site.register(Votes)
admin.site.register(TopicSuggest)



