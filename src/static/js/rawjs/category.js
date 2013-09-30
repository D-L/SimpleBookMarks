//页面内引用的部分
//1. my.tpl中的引用
function my_show_newcat(){ //打开新建对话框
	hide($("#msg-newcat"));
	$("#modal-newcat").modal();
} 
function my_show_delcat(){ //打开删除对话框
	hide($("#msg-delcat"));
	$("#modal-delcat").modal();
} 
function my_confirm_newcat(){ //新建按钮
	createcategory_i($("#newcat-title").val(),
		function(){
			showmessage($("#successmsg-newcat"),"新的收藏夹已创建");
			setTimeout(reload,1000);
		},
		function(msg){showmessage($("#msg-newcat"),msg);}
	);
}
function my_confirm_delcat(){ //删除按钮
	delcategory_i($("#delcat-title").val(),
		function(){
			showmessage($("#msg-delcat"),'成功删除了此收藏夹');
			setTimeout(reload,1000);
		},
		function(msg){showmessage($("#msg-delcat"),msg);}
	);
}
//=====================================================
//交互的部分
function createcategory_i(title,successfunc,errorfunc){
	/*
		successfunc -> func()
		errorfunc -> func(errormsg)
	*/
	function success(msg){
		if (msg.noauth) return home();
        if (msg.error && errorfunc) return errorfunc(msg.error);
		if (successfunc) successfunc();
	}
	function error(_,_,msg){if (errorfunc) errorfunc(msg);}
	$.ajax({ 
		'url' : '/0.1/newcat/',
		'type' : 'POST',
		'data' : {'title':title},
		'dataType' : 'json',
		'success' : success,
		'error' : error,
		'timeout' : 10000
	});
	return false;
}

function delcategory_i(category,successfunc,errorfunc){
	/*
		successfunc -> func()
		errorfunc -> func(errormsg)
	*/
	function success(msg){
		if (msg.noauth) return home();
        if (msg.error && errorfunc) return errorfunc(msg.error);
		if (successfunc) successfunc();
	}
	$.ajax({ 
		'url' : '/0.1/delcat/',
		'type' : 'POST',
		'data' : {'category':category},
		'dataType' : 'json',
		'success' : success,
		'error' : function (_,_,data){if (errorfunc) errorfunc(data);},
		'timeout' : 10000
	});
	return false;
}
