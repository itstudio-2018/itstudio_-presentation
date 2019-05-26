//start头部所有动画效果（点开网页开始3s动画，nav导航栏整页定位，状态查询）
//点击加入我们弹出报名表单
$('.nav').click(function(e){
    var target  = $(e.target);
    if(target.is('.join')){
        $(".joinDetail").show();
    }
    if(!target.is('.joinDetail *') && !target.is('.join')){
        $(".joinDetail").hide();
    }
    if(target.is('.joinState')){
        $(".joinStateDetail").show();
    }
    if(!target.is('.joinStateDetail *') && !target.is('.joinState')){
        $(".joinStateDetail").hide();
    }
})
$(function(){
    let team_top =$(".team").offset().top;
    let member_top =$(".member").offset().top;
    let work_top =$(".work").offset().top;
    let event_top =$(".event").offset().top;
    let message_top =$(".message").offset().top;
    $(".menu ul li").eq(0).click(function(){
        $("html,body").animate({scrollTop:team_top - 100},500);
    })
    $(".menu ul li").eq(1).click(function(){
        $("html,body").animate({scrollTop:member_top +360},500);
    })
    $(".menu ul li").eq(2).click(function(){
        $("html,body").animate({scrollTop:work_top + 150},500);
    })
    $(".menu ul li").eq(3).click(function(){
        $("html,body").animate({scrollTop:event_top - 50},500);
    })
    $(".menu ul li").eq(4).click(function(){
        $("html,body").animate({scrollTop:message_top + 100},500);
    })
})



//***侧边卡片弹出，隐藏卡片显示(点击了解更多)
//隐藏部门显示
$('body').click(function(e){
    var target  = $(e.target);
    if(target.is('.moreDepartment')){
        $(".DepartmentsDetail").show();
    }
    if(!target.is('.DepartmentsDetail *') && !target.is('.moreDepartment')){
        $(".DepartmentsDetail").hide();
    }
})
//隐藏的网页作品显示
$('body').click(function(e){
    var target  = $(e.target);
    if(target.is('.moreWorks')){
        $(".worksDetail").animate({left:'0px'});
    }
    if(!target.is('.worksDetail *') && !target.is('.moreWorks')){
        $(".worksDetail").animate({left:'-3000px'});
    }
})
//网页作品弹出的卡片点击切换一二页
$(".pointer1").click(function(){
    if($(".pointer1").hasClass("pointerColor")){
    }else{
        $(".pointer2").removeClass("pointerColor");
        $(".pointer1").addClass("pointerColor");
        $(".firstLine1").removeClass("lineChange");
        $(".secondLine1").removeClass("lineChange");
        $(".firstLine2").addClass("lineChange");
    }
})
$(".pointer2").click(function(){
    if($(".pointer2").hasClass("pointerColor")){
    }else{
        $(".pointer1").removeClass("pointerColor");
        $(".pointer2").addClass("pointerColor");
        $(".firstLine2").removeClass("lineChange");
        $(".secondLine1").addClass("lineChange");
        $(".firstLine1").addClass("lineChange");
    }
})



//**memeber成员照片展示动画效果
//member中滑行条拖动（年级条xuanze）
//使timeCar（滑块）可拖动
$.Move($('#timeCar'))
$(".pictureBox").eq(0).show().siblings().hide();
$(".teamName").click(function(){
    let number =$(this).index();
    if($(".pictureBox").eq(number).children().length >0){
        $(".pictureBox").eq(number).show();
        $(".pictureBox").eq(number).siblings().hide();
    }else{
        $(".pictureBox").eq(number).siblings().hide();
    }
})
$(".pictureBox li").eq(0).addClass("pictureLargen");
$("#left").click(function(){
    if($(".pictureLargen").index() < $(".pictureBox li").index()){
        $(this).removeClass("pictureLargen");
        $(this).next().addClass("pictureLargen")
    }
})


//**work作品模块中点击移动并且放大动画效果
$(".work1").click(function(){
    if($(this).hasClass("workMove1")){
    }else{
        $(this).addClass("workMove1")
        $(this).siblings().removeClass("workMove2 workMove3 workMove4")
    }
})
$(".work2").click(function(){
    if($(this).hasClass("workMove2")){
    }else{
        $(this).addClass("workMove2")
        $(this).siblings().removeClass("workMove1 workMove3 workMove4")
    }
})
$(".work3").click(function(){
    if($(this).hasClass("workMove3")){
    }else{
        $(this).addClass("workMove3")
        $(this).siblings().removeClass("workMove1 workMove2 workMove4")
    }
})
$(".work4").click(function(){
    if($(this).hasClass("workMove4")){
    }else{
        $(this).addClass("workMove4")
        $(this).siblings().removeClass("workMove1 workMove2 workMove3")
    }
})



//**event大事件动画效果
//event模块事件点击后变大
$(".eventsDetailBox li").click(function(){
    if($(this).hasClass("eventsBackground")){
    }else{
        $(this).siblings().removeClass("eventsBackground");
        $(this).addClass("eventsBackground");
    }
});
let preNumber = 0;
$(".eventsLineBox ul li").click(function(){
    let number =$(this).index();
    if(number === preNumber){
        return null;
    }else {
        $(this).append(`<div></div>`);
        $(this).siblings().find("div").remove();
        $(".eventsDetailBox").eq(preNumber).hide();
        $(".eventsDetailBox").eq(number).show();
        preNumber = number;
    }
});
//event滚动
$(document).ready(function() {
  
    //    $("html").niceScroll();  // The document page (html)
        
        $("#eventsDetailboxscroll").niceScroll({
          touchbehavior:false,
          cursorcolor:"#E3CCA3",
          cursoropacitymax:0.7,
          cursorwidth:11,
          cursorborder:"none",
          cursorborderradius:"8px",
          background:"#F3DCB3",
          autohidemode:"scroll"
        }) // MAC like scrollbar
      });
    
      function doRemove(name) {
        $(name).getNiceScroll().remove();
      };
      
      var vis = true;
      
      function toggleVisibility() {
        vis = !vis;
        var ns = $("#boxscroll").getNiceScroll();
        (vis) ? ns.show() : ns.hide();  
      }
      
      function toggleDiv() {
        var dv = $("#boxscroll"); 
      var vv = (dv.css('display')!='none');
        (vv) ? dv.hide() : dv.show();
    //	var ns = dv.getNiceScroll();
    //	ns.resize();
      }
    



//**message评论模块动画效果
//message模块评论框滚动条
$(document).ready(function() {
  
    //    $("html").niceScroll();  // The document page (html)
        
        $("#boxscroll").niceScroll({
          touchbehavior:false,
          cursorcolor:"#E3CCA3",
          cursoropacitymax:0.7,
          cursorwidth:11,
          cursorborder:"none",
          cursorborderradius:"8px",
          background:"#F3DCB3",
          autohidemode:"scroll"
        }) // MAC like scrollbar
      });
    
      function doRemove(name) {
        $(name).getNiceScroll().remove();
      };
      
      var vis = true;
      
      function toggleVisibility() {
        vis = !vis;
        var ns = $("#boxscroll").getNiceScroll();
        (vis) ? ns.show() : ns.hide();  
      }
      
      function toggleDiv() {
        var dv = $("#boxscroll"); 
      var vv = (dv.css('display')!='none');
        (vv) ? dv.hide() : dv.show();
    //	var ns = dv.getNiceScroll();
    //	ns.resize();
      }

//message验证码刷新
function changeverify(){ 
    $("#ident").attr("src","http://39.96.208.176/captcha//codePic?flag="+Math.random()); 
}


