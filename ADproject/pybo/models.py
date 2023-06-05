from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    modify_count = models.IntegerField() # 질문 수정 횟수 추가

    def __str__(self):
        data = f"\n작성자 : {self.author}\n제목 : {self.subject}\n내용 : {self.content}\n작성일 : {self.create_date}\n수정일 : {self.modify_date}\n추천 : {self.voter}\n수정횟수 : {self.modify_count}\n========"
        return data


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    modify_count = models.IntegerField() # 답변 수정 횟수 추가


    def __str__(self):
        data = f"\n작성자 : {self.author}\n질문글 : {self.question.subject}\n질문내용 : {self.question.content}\n답변내용 : {self.content}\n작성일 : {self.create_date}\n수정일 : {self.modify_date}\n추천 : {self.voter}\n수정횟수 : {self.modify_count}\n========"
        return data


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    modify_count = models.IntegerField() # 댓글 수정 횟수 추가
