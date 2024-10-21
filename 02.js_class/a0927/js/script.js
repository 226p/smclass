$(function(){
  let count=1;
  let total=0;
  let avg=0;
  let id_num;
  let temp=0;
  let tr_this;
    $.ajax({
      url:"js/stuData.json",
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        var stu_data = ""
        for(var i = 0; i<data.length;i++){
          count++
          total = data[i].kor+data[i].eng+data[i].math;
          avg = (total/3).toFixed(2);
          console.log(total);
          console.log(avg);
          
          stu_data += `<tr id='${data[i].no}'>`;
          stu_data += `<td>${data[i].no}</td>`;
          stu_data += `<td>${data[i].name}</td>`;
          stu_data += `<td>${data[i].kor}</td>`;
          stu_data += `<td>${data[i].eng}</td>`;
          stu_data += `<td>${data[i].math}</td>`;
          stu_data += `<td>${total}</td>`;
          stu_data += `<td>${avg}</td>`;
          stu_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`;
          stu_data += `</tr>`;

          console.log(stu_data);
          
          $("#tbody").html(stu_data);}

          $(document).on("click",".delBtn", function(){
            id_num = $(this).closest("tr").attr("id")
            if(confirm(id_num+"번 학생 성적을 삭제하시겠습니까?")){
              $("#"+id_num).remove();
              alert(id_num+"번 학생 성적이 삭제되었습니다.")
            };//데이터 삭제 이벤트
         });//for문(데이터 목록)


             $(document).on("click","#create", function(){
              if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
              alert("데이터를 입력해야 저장이 가능합니다.");
              return false;
              };

              alert("학생 성적을 추가하시겠습니까?");
              let name = $("#name").val();
              let kor = Number($("#kor").val());
              let eng = Number($("#eng").val());
              let math = Number($("#math").val());

              total = kor+eng+math;
              avg = (total/3).toFixed(2);

              var stu_data = ""
              stu_data += `'<tr id='${count}'>'`;
              stu_data += `<td>${count}</td>`;
              stu_data += `<td>${name}</td>`;
              stu_data += `<td>${kor}</td>`;
              stu_data += `<td>${eng}</td>`;
              stu_data += `<td>${math}</td>`;
              stu_data += `<td>${total}</td>`;
              stu_data += `<td>${avg}</td>`;
              stu_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`;
              stu_data += `</tr>`;

              $("#tbody").append(stu_data);

              $("#name").val("");
              $("#kor").val("");
              $("#eng").val("");
              $("#math").val("");
              count++;
            });//추가 버튼 이벤트
    

            $(document).on("click",".updateBtn",function(){
              //수정버튼 클릭 되어 있는지 확인
              if(temp==1){
                alert("수정완료 또는 수정취소 버튼을 먼저 클릭하십시오.")
                return false;
              }
              tr_this = $(this)
              tr_this.css({"color":"red"});
              
              id_num = $(this).closest("tr").attr("id");  //★★★ 위치를 잘 잡아줘야 됨

              alert("수정을 시작합니다.");
              $("#create, #update, #updateCancel").toggle();
              temp=1;

              let u_data = $(this).closest("tr");
                console.log(u_data.children("td:eq(1)").text());
                console.log(u_data.children("td:eq(2)").text());
                console.log(u_data.children("td:eq(3)").text());
                console.log(u_data.children("td:eq(4)").text());

              $("#name").val(u_data.children("td:eq(1)").text());
              $("#kor").val(u_data.children("td:eq(2)").text());
              $("#eng").val(u_data.children("td:eq(3)").text());
              $("#math").val(u_data.children("td:eq(4)").text());
            });//수정 버튼 이벤트


            $(document).on("click","#update",function(){
              if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
              alert("데이터를 입력해야 저장이 가능합니다.");
              return false;
              };
              tr_this.css({"color":"black"});

              let name = $("#name").val();
              let kor = Number($("#kor").val());
              let eng = Number($("#eng").val());
              let math = Number($("#math").val());

              total = kor+eng+math;
              avg = (total/3).toFixed(2);

              var stu_data = ""
              stu_data += `<td>${id_num}</td>`;
              stu_data += `<td>${name}</td>`;
              stu_data += `<td>${kor}</td>`;
              stu_data += `<td>${eng}</td>`;
              stu_data += `<td>${math}</td>`;
              stu_data += `<td>${total}</td>`;
              stu_data += `<td>${avg}</td>`;
              stu_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`;

              $("#"+id_num).html(stu_data);
              count++;

              alert("수정이 완료되었습니다.");
              $("#create, #update, #updateCancel").toggle();
              temp==1;

              $("#name").val("");
              $("#kor").val("");
              $("#eng").val("");
              $("#math").val("");
              temp=0;
            });//수정완료 버튼 이벤트


            $(document).on("click","#updateCancel",function(){
              alert("수정을 취소합니다.");
              tr_this.css({"color":"black"});
              $("#create, #update, #updateCancel").toggle();

              $("#name").val("");
              $("#kor").val("");
              $("#eng").val("");
              $("#math").val("");
              temp=0;
            });//수정취소 버튼 이벤트

        
      }//성공할 시 ~
      ,
      error:function(){
        alert("실패!");
      }//실패할 시 ~
    }); //ajax 선언
});