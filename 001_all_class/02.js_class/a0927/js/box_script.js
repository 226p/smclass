let num=0;
let num2=0;
$(function(){
  $("#right").click(function(){
    //alert("우우");
    if(num>=900){
      alert("오른쪽 끝에 도달했습니다. 우측 이동이 불가합니다.");
      return false;
    }
    
    $("#box").stop();
    num += 100;
    num2 += 360;
    $("#box").animate({
      left:num, "rotate":num2+"deg"
    },1000);

  });//우측 버튼 이벤트


  $("#left").click(function(){
    //alert("좌좌");
    if(num<=0){      
      alert("왼쪽 끝에 도달했습니다. 좌측 이동이 불가합니다.");
      return false;
    }
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left:num, "rotate":num2+"deg"
    },1000);

  });//좌측 버튼 이벤트
});//제이쿼리 선언