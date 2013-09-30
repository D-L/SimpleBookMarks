//一些my.tpl上要用到的按钮功能
//等待的窗口
function show_wait(cb){
	//cb: func(successfunc,errorfunc)
	function success(){ $("#modal-wait").modal('hide'); }
	function error(msg){ 
		$("#errormsg-wait").html(msg);
		show($("#errormsg-wait"));
	}
	hide($("#errormsg-wait")); //首先隐藏这个错误窗口
    $("#modal-wait").modal();
	cb(success,error);
}
function my_show_search(){
	$("#searchword").val("");
	$("#modal-search").modal();
	$("#searchword").trigger('focus');
}
function manual_add(){
	$("#modal-add").modal();
	$("#url-add").trigger('focus');
}

function try_to_get_title(){
	//1.根据判断是否含有Title,含有就算了
	var title = $('#form-add > input[name="title"]').val();
	if (title) return;
	//2.进行标题获取了
	var url = $("#url-add").val();
	$.ajax({ 
		'url' : '/0.1/gettitle/',
		'type' : 'POST',
		'data' : {'url':url},
		'dataType' : 'json',
		'success' : function(msg){
			if (msg.ok){ //确定完成了的
				var m = $('#form-add > input[name="title"]').val();
				if (m) return; //已经填写好了
				$('#form-add > input[name="title"]').val(msg.title);
			}
		},
		'timeout' : 5000
	});
}

function my_confirm_add(){
	addbookmark_i(
		$("#form-add"),
		function (){ //success
			showmessage($('#successmsg-add'),'添加更新');
			setTimeout(reload,800);
		},
		function (msg){showmessage($('#errormsg-add'),msg);}
	);
}

function my_show_import(){
	$("#modal-import").modal();
}

//编辑的部分
function loadbookmark(bid,cbsuccess,cberror){
	function error(_,_,data){cberror(data);}
	$.ajax({ 
		'url' : '/0.1/get/',
		'type' : 'POST',
		'data' : {'bookmarkid':bid},
		'dataType' : 'json',
		'success' : cbsuccess,
		'error' : error,
		'timeout' : 10000
	});
}
function my_show_edit(bid){
	show_wait(function(cbsuccess,cberror){
		loadbookmark(bid,
			function(msg){
				if (msg.noauth) return home();
				if (msg.error) return cberror(msg.error);	
				if (msg.ok){
					cbsuccess();
					my_show_edit_i(msg);
				}
			},
			cberror
		);
	});
}
function my_show_edit_i(bookmark){ //显示编辑的对话框
	$('#form-edit > input[name=bookmarkid]').val(bookmark.id);
	$('#form-edit > input[name=title]').val(bookmark.title);
	$('#form-edit > select').val(bookmark.cid);
	$('#form-edit > input[name=tag]').val(bookmark.tag);
	$('#form-edit > textarea').html(bookmark.notes);
	$('#form-edit > textarea').attr('rows',3);
	//恢复成原始态
	hide($("#successmsg-edit"));
	hide($("#errormsg-edit"));
	show($("#form-edit"));
	$("#modal-edit").modal();
}

function my_confirm_edit(){
	updatebookmark_i(
		$("#form-edit"),
		function (){ //success
			showmessage($('#successmsg-edit'),'成功更新');
			setTimeout(reload,800);
		},
		function (msg){showmessage($('#errormsg-edit'),msg);}
	);
}
//====================移动的=====================
function k_confirm_move(){
	function hidemodal(){$("#modal-move").modal('hide');}
	movebookmark_i(
		$("#form-move"),
		function (){ //success
			showmessage($('#successmsg-move'),'成功更新');
			setTimeout(hidemodal,800);
		},
		function (msg){showmessage($('#errormsg-move'),msg);}
	);
}
function my_confirm_move(){
	movebookmark_i(
		$("#form-move"),
		function (){ //success
			showmessage($('#successmsg-move'),'成功更新');
			setTimeout(reload,800);
		},
		function (msg){showmessage($('#errormsg-move'),msg);}
	);
}
function my_show_move(){
	//显示要移动的数目.
	var bids = [];
	$.each($("tr.op td.bulk i"),function(i,o){
		if ($(o).hasClass('icon-check')) bids.push($(o).attr('bid'));
	});
	if (bids.length < 1) return;
	$("#bookmarkid-move").val(bids.join(','));
	$("#modal-move").modal();
}
//====================删除的=====================
function my_show_del(bid){ //显示删除的窗口
	show($("#btns-del")); //按钮，一旦按下则不可见了。
	//需要删除的标题
	$("#message-del").text($("#title_"+bid).html());
	show($("#msg-del"));
	$("#bookmarkid-del").val(''+bid);
	hide($("#successmsg-del")); //成功的消息
	hide($("#errormsg-del"));   //错误的消息
	$("#modal-del").modal();
}

function my_show_bulkdel(){ //显示批量删除的窗口
	//显示要删除的数目.
	var bids = [];
	$.each($("tr.op td.bulk i"),function(i,o){
		if ($(o).hasClass('icon-check')) bids.push($(o).attr('bid'));
	});
	if (bids.length < 1) return;

	show($("#btns-bulkdel")); //按钮，一旦按下则不可见了。
	$("#message-bulkdel").text('已选中'+bids.length+'条记录');
	show($("#msg-bulkdel"));
	$("#bookmarkid-bulkdel").val(bids.join(','));
	hide($("#successmsg-bulkdel")); //成功的消息
	hide($("#errormsg-bulkdel"));   //错误的消息
	$("#modal-bulkdel").modal();
}

function my_confirm_del(){ delbookmarkconfirm_i('del',reload); }
function my_confirm_bulkdel(){ delbookmarkconfirm_i('bulkdel',reload); }

function k_confirm_del(){
	delbookmarkconfirm_i('del',function(){
		hide($("#tr_"+$("#bookmarkid-del").val()));
		var l = parseInt($("#count").text())-1;
		if (l > 0) $("#count").text(l);
	});
}

function k_confirm_bulkdel(){
	delbookmarkconfirm_i('bulkdel',function(){
		var bids = $("#bookmarkid-bulkdel").val().split(',');
		for(var i=0; i < bids.length; i++)
			hide($("#tr_"+bids[i]));

		var l = parseInt($("#count").text())-1;
		if (l > 0) $("#count").text(l);
		if (l < 1) $("#count").text(0);
	});
}

function delbookmarkconfirm_i(prefix,succfunc){ //删除按钮的对应
	function hidemodal(){$("#modal-"+prefix).modal('hide');}
	delbookmark_i(
		$("#bookmarkid-"+prefix).val(),
		function (){ //success
			hide($("#msg-"+prefix));
			hide($("#btns-"+prefix)); //避免再次提交
			showmessage($('#successmsg-'+prefix),'成功删除');
			setTimeout(
				function(){
					hidemodal();
					if (succfunc) succfunc();
				},800
			);
		},
		function (msg){showmessage($('#errormsg-'+prefix),msg);}
	);
}
//=====================================================
//交互的部分
function movebookmark_i(jform,successcb,errorcb){
	/*
		jform ->JQuery的form
		successcb -> func()
		errorcb -> func(errormsg)
		更新收藏
	*/
	function error(_,_,data){if(errorcb) errorcb(data);}
	function success(msg){
		if (msg.noauth) return home();
		if (msg.error && errorcb) return errorcb(msg.error);
		if (msg.ok && successcb) successcb();
	}
	$.ajax({ 
		'url' : '/0.1/move/',
		'type' : 'POST',
		'data' : jform.serialize(),
		'dataType' : 'json',
		'success' : success,
		'error' : error,
		'timeout' : 10000
	});
}

function delbookmark_i(bookmarkid,successcb,errorcb){
	/*
		多个bookmarkid之间用,连接
		successcb -> func()
		errorcb -> func(errormsg)
	*/
	function error(_,_,data){ if (errorcb) errorcb(data);}
	function success(msg){
		if (msg.noauth) return home();
		if (msg.error && errorcb) return errorcb(msg.error);
		if (msg.ok && successcb) successcb();
	}
	$.ajax({ 
		'url' : '/0.1/delete/',
		'type' : 'POST',
		'data' : $.param({'bookmarkid':bookmarkid}),
		'dataType' : 'json',
		'success' : success,
		'error' : error,
		'timeout' : 10000
	});
}

function updatebookmark_i(jform,successcb,errorcb){
	/*
		jform ->JQuery的form
		successcb -> func()
		errorcb -> func(errormsg)
		更新收藏
	*/
	function error(_,_,data){if(errorcb) errorcb(data);}
	function success(msg){
		if (msg.noauth) return home();
		if (msg.error && errorcb) return errorcb(msg.error);
		if (msg.ok && successcb) successcb();
	}
	$.ajax({ 
		'url' : '/0.1/update/',
		'type' : 'POST',
		'data' : jform.serialize(),
		'dataType' : 'json',
		'success' : success,
		'error' : error,
		'timeout' : 10000
	});
}

function addbookmark_i(jform,successcb,errorcb){
	/*
		jform ->JQuery的form
		successcb -> func()
		errorcb -> func(errormsg)
		手动新增加一个
	*/
	function error(_,_,data){if(errorcb) errorcb(data);}
	function success(msg){
		if (msg.noauth) return home();
		if (msg.error && errorcb) return errorcb(msg.error);
		if (msg.ok && successcb) successcb();
	}
	$.ajax({ 
		'url' : '/0.1/manualtie/',
		'type' : 'POST',
		'data' : jform.serialize(),
		'dataType' : 'json',
		'success' : success,
		'error' : error,
		'timeout' : 10000
	});
}
