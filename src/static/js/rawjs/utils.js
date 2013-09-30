function showmessage(jnode,msg){jnode.text(msg);jnode.removeClass('hide');} //JQuery Node
function reload(){window.location.reload();}
function home(){window.location.href="/";}
function show(jnode){jnode.removeClass('hide');}
function hide(jnode){jnode.addClass('hide');}

//-----------------------
function Turnner(forefunc,backfunc){
	this.func = [forefunc,backfunc];
}; //翻转牌
Turnner.prototype.turn = function(){ //翻转一次
	func = this.func.shift();
	this.func.push(func);
	func();
}

//点击时出现操作链接,已读/未读,删除，编辑的
STATUS = {}
function updateStatus(status,value){ STATUS[status] = value;}
function getStatus(status){ return STATUS[status] }

//为了Tag提示使用
function ahead_matcher(item){
	var m = this.query.split(/,|，/);
	var w = m[m.length-1];
	if (!w) return false;
	return ~item.toLowerCase().indexOf(w.toLowerCase())
}
function ahead_sorter(items){
	var m = this.query.split(/,|，/);
	var w = m[m.length-1];
	if (!w) return [];
	w = w.toLowerCase();

	var m1 = [], m2 = [], m3 = [];
	while (item = items.shift()) {
		if (!item.toLowerCase().indexOf(w)) m1.push(item)
        else if (~item.indexOf(w)) m2.push(item)
        else m3.push(item)
	}
	return m1.concat(m2,m3);
}
function ahead_updater(item){
	var m = this.query.split(/,|，/);
	m = m.slice(0,-1)
	m.push(item);
	return m.join(',')+',';
}
