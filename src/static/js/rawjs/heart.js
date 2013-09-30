function hideoneheart(bid){
		hide($("#heartico_"+bid));
		$("#heart_"+bid).removeClass('icon-heart-empty').addClass('icon-heart');
}
function showoneheart(bid){
		show($("#heartico_"+bid));
		$("#heart_"+bid).removeClass('icon-heart').addClass('icon-heart-empty');
}
function changeoneheart(bid){ //改变某个收藏的状态.
	var h = $("#heartico_"+bid);
	if (h.hasClass('hide')) showoneheart(bid);
	else hideoneheart(bid);
}
//页面内引用的部分
//1. myheart.tpl
function cancelheart(bookmarkid){ //取消喜爱
	heart_i([bookmarkid],0,function(){
		hide($("#tr_"+bookmarkid));
		//数字减少
		$("#count").html(parseInt($("#count").text())-1);
	}); //隐藏单条
}

//2. k.tpl 搜索用的/ my.tpl中用
function bulkheart(){ //批量的喜爱/取消喜爱
	//当前不是bulk模式就退出
	if (!getStatus('bulk')) return;

	var bids = [];
	$.each($("tr.op td.bulk i"),function(i,o){
		if ($(o).hasClass('icon-check')) bids.push($(o).attr('bid'));
	});
	if (bids.length < 1) return;

	var b = $("#bulkheart > i");
	function heartok(bids){
		for(var i=0; i < bids.length; i++) showoneheart(bids[i]);
		b.attr("title","取消喜爱");
		b.removeClass('icon-heart').addClass('icon-heart-empty');
	}
	function cancelheartok(bids){
		for(var i=0; i < bids.length; i++) hideoneheart(bids[i]);
		b.attr("title","加喜爱");
		b.removeClass('icon-heart-empty').addClass('icon-heart');
	}
	//确定当前是全部喜爱，还是取消喜爱
	if (b.hasClass("icon-heart")){
		heart_i(bids,1,heartok);
	}else{
		heart_i(bids,0,cancelheartok);
	}
}

function heart(bookmarkid){ //标记某条为喜爱/不喜爱
	var h = $("#heartico_"+bookmarkid);
	var flag = 0;
	if (h.hasClass('hide')) flag = 1; //当前是不喜爱
	heart_i([bookmarkid],flag,function(bids){
		for(var i=0; i < bids.length; i++) changeoneheart(bids[i]);
	});
}
//=====================================================
//交互的部分
function heart_i(bids,flag,successfunc){
	/*
		标记为喜爱/取消喜爱.
		flag : 1,标记为喜爱
             : 0,取消喜爱
		successfunc -> func(bid);
	*/
	function success(msg){
		if (msg.noauth) return home();
		if (msg.ok && successfunc) successfunc(bids);
	}
	$.ajax({ 
		'url' : '/0.1/heart/',
		'type' : 'POST',
		'data' : $.param({'bookmarkids':bids.join(','),'flag':''+flag}),
		'dataType' : 'json',
		'success' : success,
		'timeout' : 8000
	});
	return false;
}
