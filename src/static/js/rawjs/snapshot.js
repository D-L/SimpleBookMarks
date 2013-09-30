//快照部分
function snapshot(bookmarkid){ //给某条进行拍照
	var s = $("#ss_"+bookmarkid);
	if (s.hasClass('icon-refresh')) return;
	snapshot_i(bookmarkid,function(bid){
		var s = $("#ss_"+bid);
		var p = $("#ss_"+bid).parent();
		p.attr('title','正在快照中...');
		s.removeClass('icon-camera').addClass('icon-refresh');
	});
}
//=====================================================
//交互的部分
function snapshot_i(bid,successfunc){
	/*
		给某个收藏加上快照.
		successfunc -> func(bid);
	*/
	function success(msg){
		if (msg.noauth) return home();
		if (msg.ok && successfunc) successfunc(bid);
		if (msg.error){
			$.notify(msg.error,{ position:"top center",autoHideDelay:2000});
		}
	}
	$.ajax({ 
		'url' : '/0.1/snapshot/',
		'type' : 'POST',
		'data' : {'bookmarkid':bid},
		'dataType' : 'json',
		'success' : success,
		'timeout' : 8000
	});
	return false;
}
