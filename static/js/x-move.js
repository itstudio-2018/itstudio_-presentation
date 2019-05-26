(function($){
    
    //拖拽插件,参数:id或object
    $.Move = function(_this){
        if(typeof(_this)=='object'){
            _this=_this;
        }else{
            _this=$("#"+_this);
        }
        if(!_this){return false;}
        _this.css({'position':'absolute'}).hover(function(){$(this).css("cursor","pointer");},function(){$(this).css("cursor","pointer");})
        _this.mousedown(function(e){//e鼠标事件
            var offset = $(this).offset();
            var father =$(this).parent().offset();
            var x = e.pageX - offset.left;
            _this.css({'opacity':'0.8'});
            $(document).bind("mousemove",function(ev){//绑定鼠标的移动事件，因为光标在DIV元素外面也要有效果，所以要用doucment的事件，而不用DIV元素的事件
                _this.bind('selectstart',function(){return false;});
                var _x = ev.pageX - x - father.left;//获得X轴方向移动的值
                if(_x <= 0 || _x >= 1145){
                       return;
                }else{
                _this.css({'left':_x+"px"});
                }
                
                
                var timer;
                function debounce(fn, delay){
                    clearTimeout(timer);
                    timer = setTimeout(function(){
                        fn();
                    }, delay);
                }
                
                function requestMember(){
                    console.log(_x);
                }
                document.onmousemove =() => {
                    debounce(requestMember,1000);
                }
                //$("#timeCar").on("mousemove",requestMember());
                // function requestMember(){
                //     var timer ;
                //     return function(){
                //         clearTimeout(timer);
                //         timer =setTimeout(function(){
                //               console.log(_x);
     
                //         }, 600);
                //     }
                            //   if(_x <= 342){
                            //     requestMember2017();
                            // }else if(342 < _x <= 513){
                            //     requestMember2016();
                            // }else if(513 < _x <= 684){
                            //     requestMember2015();
                            // }else if(684 < _x <= 855){
                            //     requestMember2014();
                            // }else if(855 < _x <= 1026){
                            //     requestMember2013();
                            // }else if(1026 < _x ){
                            //     requestMember2012();
                            // }
                
            });
        });
        $(document).mouseup(function(){
            $(this).unbind("mousemove");
            _this.css({'opacity':''});
        })
    };
})(jQuery)