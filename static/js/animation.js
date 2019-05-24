//点击加入我们弹出报名表单
$('.nav').click(function(e){
    var target  = $(e.target);
    if(target.is('.join')){
        $(".joinDetail").show();
    }
    if(!target.is('.joinDetail *') && !target.is('.join')){
        $(".joinDetail").hide();
    }
})



//侧边卡片弹出，隐藏卡片显示(点击了解更多)
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
        $(".worksDetail").animate({left:'-2000px'});
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



//member中滑行条拖动（年级条xuanze）
//使timeCar（滑块）可拖动
$.Move($('#timeCar'))



//event模块事件点击后变大
$(".eventsDetailBox li").click(function(){
    if($(this).hasClass("eventsBackground")){
    }else{
        $(this).siblings().removeClass("eventsBackground");
        $(this).addClass("eventsBackground");
    }
})
