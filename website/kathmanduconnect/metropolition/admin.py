from django.contrib import admin
from .models import User, Event, Forum, Hotline, Notices, Poll, Reports, Reward, Safety, Tourism, Transport, UserForum, UserNotices, UserPoll, UserVoting, Volunteer, Voting

# Register your models with the admin interface
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Forum)
admin.site.register(Hotline)
admin.site.register(Notices)
admin.site.register(Poll)
admin.site.register(Reports)
admin.site.register(Reward)
admin.site.register(Safety)
admin.site.register(Tourism)
admin.site.register(Transport)
admin.site.register(UserForum)
admin.site.register(UserNotices)
admin.site.register(UserPoll)
admin.site.register(UserVoting)
admin.site.register(Volunteer)
admin.site.register(Voting)
