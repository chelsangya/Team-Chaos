from django.db import models

class User(models.Model):
    uID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    photo = models.CharField(max_length=50)
    citienship_no = models.IntegerField()
    OTP = models.IntegerField(null=True)

class Event(models.Model):
    eID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    date = models.DateField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

class Forum(models.Model):
    fID = models.AutoField(primary_key=True)
    message = models.CharField(max_length=50)
    datetime = models.DateField()

class Hotline(models.Model):
    hID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class Notices(models.Model):
    nID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()

class Poll(models.Model):
    pID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class Reports(models.Model):
    rID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)

class Reward(models.Model):
    rID = models.AutoField(primary_key=True)
    point = models.IntegerField()
    level = models.CharField(max_length=50)

class Safety(models.Model):
    sID = models.AutoField(primary_key=True)
    issueType = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    uID = models.IntegerField()

class Tourism(models.Model):
    tID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)

class Transport(models.Model):
    tID = models.AutoField(primary_key=True)
    busName = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)

class UserForum(models.Model):
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)
    ForumfID = models.ForeignKey(Forum, on_delete=models.CASCADE)

class UserNotices(models.Model):
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)
    NoticesnID = models.ForeignKey(Notices, on_delete=models.CASCADE)

class UserPoll(models.Model):
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)
    PollpID = models.ForeignKey(Poll, on_delete=models.CASCADE)

class UserVoting(models.Model):
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)
    VotingvID = models.IntegerField()

class Volunteer(models.Model):
    vID = models.AutoField(primary_key=True)
    UseruID = models.ForeignKey(User, on_delete=models.CASCADE)
    EventseID = models.ForeignKey(Event, on_delete=models.CASCADE)

class Voting(models.Model):
    voID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
