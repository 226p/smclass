from django.db import models

class Board(models.Model):
  bno = models.AutoField(primary_key=True)   # 번호가 자동으로 1씩 증가
  id = models.CharField(max_length=100)
  # member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)    # member에 있는 데이터 가져오기
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()   # 대용량 글자 가능
  bgroup = models.IntegerField(null=True)   # bgroup : 답글 사용할 때 그룹핑
  bstep = models.IntegerField(default=0)   # bstep : 답글 사용할 때 순서
  bindent = models.IntegerField(default=0)   # bindent : 답글 사용할 때 들여쓰기
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  # btop : 가장 위쪽 공지사항

  def __str__(self):
    return f"{self.bno},{self.id},{self.btitle},{self.bdate}"