$(function(){
  var count=0;
  var num=1;
  $("#search_btn").click(function(){
    alert("검색버튼 클릭")
    let surl ="https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=ZXqxh44uenTKlnLQeKPuWyLzzNK9iSIaLOTMUMuup1hpLNFueyYme0Jxp33sxT3S%2BzdvTYHbbIsjgm2fkTLNYw%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        alert("성공");
        console.log(data.response.body.items); 
        var g_item = data.response.body.items.item; //★★★ 위치점 선정 중요!
        console.log(g_item[0].galTitle);

        var i_data = "";
        for(var i=0;i<g_item.length;i++){
          i_data += `<tr id='${count}'>`;
          i_data += `<td>${num}</td>`;
          i_data += `<td>${g_item[i].galTitle}</td>`;
          i_data += `<td>${g_item[i].galPhotographer}</td>`;
          i_data += `<td>${g_item[i].galModifiedtime}</td>`;
          i_data += `<td><img src='${g_item[i].galWebImageUrl}'></td>`;
          i_data += `</tr>`;

          count++;
          num++;
        }
        $("#tbody").html(i_data);

      },
      error:function(){
        alert("실패");
      }
    });//ajax
    
  });//search_btn 검색 버튼 클릭

});//제이쿼리 선언