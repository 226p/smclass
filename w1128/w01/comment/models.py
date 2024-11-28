from django.db import models
from board.models import Board
from member.models import Member

class Comment(models.Model):
  cno = models.AutoField(primary_key=True)
  board = models.ForeignKey(Board,on_delete=models.CASCADE)  # 부모 삭제 시 자식 삭제
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
  ccontent = models.TextField(blank=True)
  cpw = models.CharField(max_length=10,null=True)
  cdate = models.DateTimeField(auto_now=True,blank=True)

  def __str__(self):
    return f"{self.cno},{self.ccontent},{self.cdate}"

