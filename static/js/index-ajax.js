//***懒加载
$(window).on("scroll",function(){
    start()
})
 //加载函数
 function start(){
    $('img').not('[data-isLoaded]').each(function(){
      if( isShow($(this)) ){
        loadImg($(this))
      }
    })
  }
  // 判断是否进入视野的函数
  function isShow($node){
    return $node.offset().top - 200 <= $(window).height() + $(window).scrollTop()
  }
  // 格式化图片加载地址函数
  function loadImg($img){
    //setTimeout模拟延迟 测试效果用，实际环境不要加
    setTimeout(function(){
      $img.attr('src', $img.attr('data-src'))
    },3000)
     //加载过后就添加 data-isLoaded属性
      $img.attr('data-isLoaded',1)
  }



/**
 *  获取服务器URL
 * */
const ServerURL = function () {
    let __URL =  "http://39.96.208.176";  //在ajax属性内拼接
    return ()=>{
        return __URL;
    }
};
/**
 * 接口
 * */
const Url_Options = {
    MESSAGE_LIST: "\\show\\api\\comment_list\\",
    POST_MESSAGE:"\\show\\api\\comment\\",
    EVENTS_LIST: "\\show\\api\\story\\",
    MEMBER_LIST:"\\show\\api\\member\\",
    VERIFY:"\\captcha\\",
};

/***
 * 限制字数
 * @param content
 * @param number
 * @returns {*}
 */
function limitWords(content, number) {
    if(content.length >= number){
        content = content.substr(0, number) + "...";
    }
    return content;
}
function getXMLObject() {
    let xmlHttp;
    if (window.XMLHttpRequest) {
        xmlHttp=new XMLHttpRequest();
    } else {
        xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xmlHttp;
}
/***
 *  获取请求对象
 * @param url
 * @param contentType
 * @param responseType
 * @param method
 * @param data
 * @returns {Promise<any>}
 */
function getRequest(url, contentType, responseType, method, data){
    return new Promise(function (resolve, reject) {
        let xmlHttp = getXMLObject();
        xmlHttp.onreadystatechange = function () {
            if (this.readyState === 4) {
                if (this.status === 200) {
                    resolve(this.response);
                } else {
                    reject(new Error("请求失败"));
                }
            }
        };
        xmlHttp.open(method, url);
        xmlHttp.responseType = responseType;
        xmlHttp.setRequestHeader("Content-Type", contentType);
        if(method === "POST"){
            xmlHttp.send(data);
        }else{
            xmlHttp.send(null);
        }
    })
}
/***
 * 获取dom
 */
let memberShow = $(".memberShow");
/**
 * 请求member各年级成员
 * 
 * */
//获取2017级信息
function requestMember2017(){
    getRequest((ServerURL())() + Url_Options.MEMBER_LIST +"?year=2017", "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            console.log(list);
            for (let i = 0; i < list.length; i++) {
                let name = list[i]["name"];
                let department = list[i]["department"];
                let image = list[i]["image"];
                let info = list[i]["info"];
                let departmentNumber =list[i]["department_id"];
                let number = departmentNumber - 1;
                console.log(`${(ServerURL())() + Url_Options.MEMBER_LIST +"?year=2017"+image}`);
                $(".pictureBox").eq(number).append(`<li><p>${info} </p><img src=${(ServerURL())() +image}><h5> ${name} </h5></li>`);
                // console.log(year.indexOf(2015));
            }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error);
    };
}
(function loadMember() {
    requestMember2017();
})();
//获取2016级信息
function requestMember2016(){
    getRequest((ServerURL())() + Url_Options.MEMBER_LIST +"?year=2016", "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            console.log(list);
            for (let i = 0; i < list.length; i++) {
                let name = list[i]["name"];
                let department = list[i]["department"];
                let image = list[i]["image"];
                let info = list[i]["info"];
                let departmentNumber =list[i]["department_id"];
                let number = departmentNumber - 1;
                console.log(`${(ServerURL())() + Url_Options.MEMBER_LIST +"?year=2017"+image}`);
                $(".pictureBox").eq(number).append(`<li><p>${info} </p><img src=${(ServerURL())() +image}><h5> ${name} </h5></li>`);
                // console.log(year.indexOf(2015));
            }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error);
    };
}
//获取2015级信息
function requestMember2015(){
    getRequest((ServerURL())() + Url_Options.MEMBER_LIST +"?year=2015", "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            console.log(list);
            for (let i = 0; i < list.length; i++) {
                let name = list[i]["name"];
                let department = list[i]["department"];
                let image = list[i]["image"];
                let info = list[i]["info"];
                let departmentNumber =list[i]["department_id"];
                let number = departmentNumber - 1;
                console.log(`${(ServerURL())() + Url_Options.MEMBER_LIST +"?year=2017"+image}`);
                $(".pictureBox").eq(number).append(`<li><p>${info} </p><img src=${(ServerURL())() +image}><h5> ${name} </h5></li>`);
                // console.log(year.indexOf(2015));
            }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error);
    };
}
//获取2014级信息
function requestMember2014(){
    getRequest((ServerURL())() + Url_Options.MEMBER_LIST +"?year=2014", "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            console.log(list);
            for (let i = 0; i < list.length; i++) {
                let name = list[i]["name"];
                let department = list[i]["department"];
                let image = list[i]["image"];
                let info = list[i]["info"];
                let departmentNumber =list[i]["department_id"];
                let number = departmentNumber - 1;
                console.log(`${(ServerURL())() + Url_Options.MEMBER_LIST +"?year=2017"+image}`);
                $(".pictureBox").eq(number).append(`<li><p>${info} </p><img src=${(ServerURL())() +image}><h5> ${name} </h5></li>`);
                // console.log(year.indexOf(2015));
            }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error);
    };
}
/***
 * 获取dom
 */
let eventsDetailBox = $(".eventsDetailBox");
/**
 * 请求event年代大事件
 * 
 * */
function requestEvents(){
    getRequest((ServerURL())() + Url_Options.EVENTS_LIST, "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            for (let i = 0; i < list.length; i++) {
                let year = list[i]["year"];
                let title = list[i]["title"];
                let info = list[i]["info"];
                let number = year - 2014
                // console.log(year.indexOf(2015));
                $(".eventsDetailBox").eq(number).append(`<li><p> ${title} </p><span> ${info} </span></li>`);
            }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error);
    };
}
(function loadEvents() {
    requestEvents();
})();

/***
 * 获取dom
 */
let messageList = $(".messageList");
/**
 * 请求message评论列表
 * */
function requestMessage(){
    getRequest((ServerURL())() + Url_Options.MESSAGE_LIST, "application/x-www-form-urlencoded", "json", "GET").then((json)=>{
        successHandler(json);
    }, (error)=>{
        failHandler(error);
    });
    let successHandler = function (json) {
        if(json["status"] === "ok"){
            let list = json["list"];
            for (let i = 0; i < list.length; i++) {
                let content = list[i]["content"];
                let time = list[i]["time"];
                let reply =list[i]["reply"];
                $(".messageList").append(`<li><p> ${content} </p><h5>回复： ${reply} </h5><span> ${time} </span></li>`);
            }
            // console.log(messageList);
            // for(let item of messageList){
            //     let content = item["content"];
            //     let time = item["time"];
            //     console.log(time);
            //     $(".messageList").eq(i).append(`<li><p> ${content} </p><span> ${time} </span></li>`);
            // }
        }else{
            console.log(json["status"])
        }
    };
    let failHandler = function (error) {
        console.log(error.message);
    };
}
(function loadMessage() {
    requestMessage();
})();




/**
 * 发表评论，验证验证码
 * */
$(".messageSubmit").click(function() {

	if ($(".messageText textarea").val() =='') {
		alert("留言不能为空！");
		changeverify();
	} else if ($(".verify input").val()=='') {
		alert("请输入验证码！");
		changeverify();
    } 
        var messageObject ={
                content: $(".messageText textarea").val(),
                code: $(".verify input").val(),
        };

		$.ajax({
			type: "POST",
            url:" http://39.96.208.176/show/api/comment/",
            contentType:"application/json;charset=utf-8",
			timeout: 5000,
			data: JSON.stringify(),
			dataType: "json",
			//发送成功可以返回的东西
			success: function(data) {
				if (data.statusC == 'ok') {
					alert("留言发表成功!");
					close_comment();
					location.reload();
				} else if (data.statusC == 'code_error') {
					alert("验证码错误！");
					changeverify();
				} else {
					alert("留言提交失败！");
					changeverify();
				}
			},
			error: function(jqXHR) {
				// alert("服务器错误请重试，错误代码：" + jqXHR.status);
				alert("留言提交失败！");
			},
		});

})

// $(".messageSubmit").click(function postMessage(){
//     var model = [];
//     model.push($(".verify input").val(), $(".messageText textarea").val());
//     console.log(JSON.stringify(model))
//     getRequest((ServerURL())() + Url_Options.POST_MESSAGE, "application/x-www-form-urlencoded", "json", "send","JSON.stringify(model)").then((json)=>{
//         successHandler(json);
//     }, (error)=>{
//         failHandler(error);
//     });
//     let successHandler = function (json) {
//         alert("success!!");
//     };
//     let failHandler = function (error) {
//         alert("failed~~");
//     };
// })
