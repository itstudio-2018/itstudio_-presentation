//点击加入我们弹出报名表单
$(".join").click(function(){
    $(".joinDetail").toggle();
})

//team中左右点击后出现部门介绍和社团介绍，中间圈圈旋转180°
$(".teamLeft").click(function(){
    $(".Departments").toggle();
    $(".teamLeft").animate({opacity:'1'});
})
$(".teamRight").click(function(){
    $(".Definition").toggle();
    $(".teamRight").animate({opacity:'1'})
})
$(".teams").click(function(){
    if($(".rolling").hasClass("rotate")){
        $(".rolling").removeClass("rotate");
        $(".rolling").addClass("rotate1");
    }else{
        $(".rolling").removeClass("rotate1");
        $(".rolling").addClass("rotate");
    }
})
//侧边卡片弹出
// $(".team").click(function(e){
//     var target  = $(e.target);
//     if(!target.is('.DepartmentsDetail')){
//         $(".DepartmentsDetail").animate({left:'-2000px'});
//     }
//     if(target.is('.DepartmentsMore')){
//         $(".Departmentstail").animate({left:'0px'});
//     }
// })
// $(".team").click(function(e){
//     var target  = $(e.target);
//     if(!target.is('.DefinitionDetail')){
//         $(".DefinitionDetail").animate({left:'-2000px'});
//     }
//     if(target.is('.DefinitionMore')){
//         $(".DefinitionDetail").animate({left:'0px'});
//     }
// })

$(".work").click(function(e){
    var target  = $(e.target);
    if(!target.is('.worksDetail')){
        $(".worksDetail").animate({left:'-2000px'});
    }
    if(target.is('.moreWorks')){
        $(".worksDetail").animate({left:'0px'});
    }
    if(target.is('.pointer')){
        $(".worksDetail").animate({left:'0px'});
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