//点击加入我们弹出报名表单
$(".join").click(function(){
    $(".joinDetail").toggle();
})

//team中左右点击后出现部门介绍和社团介绍，中间圈圈旋转180°
$(".teamLeft").click(function(){
    $(".Departments").toggle();
    $(".teamLeft").animate({opacity:'1'})
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
$(".DepartmentsMore").click(function(){
    $(".DepartmentsDetail").animate({left:'0px'},function(){
        if($(".DepartmentsDetail").left == 0){
            
        }
        $(document).click(function(e){
            var target  = $(e.target);
            if(!target.is('.DepartmentsDetail')){
                $(".DepartmentsDetail").animate({left:'-2000px'});
            }
        })
    })
})
$(".DefinitionMore").click(function(){
    $(".DefinitionDetail").animate({left:'0px'},function(){
        $(document).click(function(e){
            var target  = $(e.target);
            if(!target.is('.DefinitionDetail')){
                $(".DefinitionDetail").animate({left:'-2000px'});
            }
        })
    })
})
$(".moreWorks").click(function(){
    $(".worksDetail").animate({left:'0px'},function(){
        $(document).click(function(e){
            var target  = $(e.target);
            if(!target.is('.worksDetail')){
                $(".worksDetail").animate({left:'-2000px'});
            }
        })
    })
})
