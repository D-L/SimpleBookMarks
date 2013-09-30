(function(){
	var style=""+
	".yat-size{font-size:15px;padding:8px 35px 8px 14px;margin-bottom:10px;text-shadow:0 1px 0 rgba(255,255,255,0.5);color:#3a87ad;background-color:#d9edf7;border:1px solid #bce8f1;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;z-index:100000000;*zoom:1;position:fixed;top:5px;left:4%;width:90%}"+
	".yat{padding:8px 35px 8px 14px;margin-bottom:10px;text-shadow:0 1px 0 rgba(255,255,255,0.5);color:#3a87ad;background-color:#d9edf7;border:1px solid #bce8f1;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;z-index:100000000;*zoom:1;position:fixed;top:5px;left:25%}"+
	".yat-td{width:480px}"+
	".yat-sp{width:100px}"+
	".yat-err{color:#b94a48;background-color:#f2dede;border:1px solid #eed3d7}"+
	".yat-select,.yat-textarea,.yat-input{font-size:14px !important;display:inline-block;height:28px;width:100%;padding:4px;margin-bottom:9px;line-height:28px;color:#555}"+
	".yat-textarea,.yat-input{background-color:#fff;border:1px solid #ccc;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}"+
	".yat-btn{cursor:pointer;-webkit-appearance:button;*padding-top:2px;*padding-bottom:2px;display:inline-block;*display:inline;padding:4px 10px 4px;margin-bottom:0;*margin-left:.3em;font-size:13px;line-height:18px;*line-height:20px;color:#333;text-align:center;text-shadow:0 1px 1px rgba(255,255,255,0.75);vertical-align:middle;cursor:pointer;background-color:#f5f5f5;*background-color:#e6e6e6;background-image:-ms-linear-gradient(top,#fff,#e6e6e6);background-image:-webkit-gradient(linear,0 0,0 100%,from(#fff),to(#e6e6e6));background-image:-webkit-linear-gradient(top,#fff,#e6e6e6);background-image:-o-linear-gradient(top,#fff,#e6e6e6);background-image:linear-gradient(top,#fff,#e6e6e6);background-image:-moz-linear-gradient(top,#fff,#e6e6e6);background-repeat:repeat-x;border:1px solid #ccc;*border:0;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);border-color:#e6e6e6 #e6e6e6 #bfbfbf;border-bottom-color:#b3b3b3;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;filter:progid:dximagetransform.microsoft.gradient(startColorstr='#ffffff',endColorstr='#e6e6e6',GradientType=0);filter:progid:dximagetransform.microsoft.gradient(enabled=false);*zoom:1;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05);box-shadow:inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05)}"+
	".yat-primary{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#0074cc;*background-color:#05c;background-image:-ms-linear-gradient(top,#08c,#05c);background-image:-webkit-gradient(linear,0 0,0 100%,from(#08c),to(#05c));background-image:-webkit-linear-gradient(top,#08c,#05c);background-image:-o-linear-gradient(top,#08c,#05c);background-image:-moz-linear-gradient(top,#08c,#05c);background-image:linear-gradient(top,#08c,#05c);background-repeat:repeat-x;border-color:#05c #05c #003580;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);filter:progid:dximagetransform.microsoft.gradient(startColorstr='#0088cc',endColorstr='#0055cc',GradientType=0);filter:progid:dximagetransform.microsoft.gradient(enabled=false)}"+
	".yat-large{padding:9px 14px;font-size:16px;line-height:normal;-webkit-border-radius:5px;-moz-border-radius:5px;border-radius:5px}"+
	".yat-btn.yat-large{*padding-top:7px;*padding-bottom:7px}"+
	".yat-a{color:#08c;text-decoration:none;font-size:14px;}"+
	".yat-a:hover{color:#005580;text-decoration:underline}"+
	".yat-label{color:#005580;display:block;float:left;font-size:14px;font-weight:bold;margin:0;}"+
	".yat-right{float:right}"+
	".yat-textarea{overflow:auto;height:auto;vertical-align:top}"+
	".yat-textarea:focus,.yat-input:focus{border-color:rgba(82,168,236,0.8);outline:0;outline:thin dotted \9;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(82,168,236,0.6);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(82,168,236,0.6);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(82,168,236,0.6)}";
	var st = document.createElement('style');
	st.id = '_yat_style';
	st.type = 'text/css';
	if (st.styleSheet){
		st.styleSheet.cssText = style;
	}else{
		st.innerHTML= style;
	}
	//一定要加载在最大的窗口上面
	(document.getElementsByTagName('head')[0]||document.body).appendChild(st); //增加一个style进去.
	//增加函数构造
	YAT_RUNNER = function(){
		this.img = undefined; //发出的URL操作.
	}
	YAT_RUNNER.prototype.getselect = function(){
	    if (window.getSelection) return window.getSelection();
    	if (document.getSelection) return document.getSelection();
	    if (document.selection) return document.selection.createRange().text;
		return '';
	}
	YAT_RUNNER.prototype.bind = function(obj,type,fn) {
		if (!obj) return;
		if ( obj.attachEvent ) {
			obj['e'+type+fn] = fn;
			obj[type+fn] = function(){obj['e'+type+fn]( window.event );}
			obj.attachEvent( 'on'+type, obj[type+fn] );
		}else{
			obj.addEventListener( type, fn, false );
		}
	}
	YAT_RUNNER.prototype.geturl= function() {
		var s = [],
			add = function( key, value ) {
				if (!value) return;
				s[ s.length ] = encodeURIComponent( key ) + "=" + encodeURIComponent( value );
			};
		var t = this.gnid('_yat_url'); add(t.name,t.value);
		t = this.gnid('_yat_category'); add(t.name,t.value);
		t = this.gnid('_yat_heart'); if (t.checked) add(t.name,'1');
		t = this.gnid('_yat_title'); add(t.name,t.value);
		t = this.gnid('_yat_tag'); add(t.name,t.value);
		t = this.gnid('_yat_notes'); add(t.name,t.value);
		return '{{httpdomain}}/jstie/?'+s.join( "&" ).replace(/%20/g,"+");
	}
	YAT_RUNNER.prototype.gnid = function(aid){ return document.querySelector('#'+aid); }
	YAT_RUNNER.prototype.hide = function(n){ n.style.display = "none";}
	YAT_RUNNER.prototype.show = function(n){ n.style.display = "block";}
	/*
	YAT_RUNNER.prototype.hide = function(n){ n.style.visibility='hidden';}
	YAT_RUNNER.prototype.show = function(n){ n.style.visibility='visible';}
	*/
	YAT_RUNNER.prototype.init = function(){ //初始化只进行一次的
		//notes的输入口变化大小
		this.bind(this.gnid('_yat_notes'),'focus',function(evt){
			if (evt.target) evt.target.rows=8;
			else event.srcElement.rows = 8;
		});
		//绑定按钮
		function get_i(obj){ return function(){obj.get();}; }
		function close_i(obj){ return function(){obj.hide(obj.gnid('_yat_tie'));obj.hide(obj.gnid('_yat_msg'));};}
		this.bind(this.gnid('_yat_get'),'click',get_i(this));
		this.bind(this.gnid('_yat_close'),'click',close_i(this));
		//新建按钮
		function new_i(obj){ return function(){
			//然后释放这个窗口
			//1. 释放style
			try{document.head.removeChild(obj.gnid('_yat_style'));}catch(err){}
			try{document.body.removeChild(obj.gnid('_yat_style'));}catch(err){}
			//2. 释放
			try{document.body.removeChild(obj.gnid('_yat_tie'));}catch(err){}
			try{document.body.removeChild(obj.gnid('_yat_msg'));}catch(err){}
			try{document.body.removeChild(obj.gnid('_yat_info'));}catch(err){}
			//3. script
			try{document.body.removeChild(obj.gnid('_yat_script'));}catch(err){}
			//4. image存在的了
			try{if (obj.img) document.body.removeChild(this.img);}catch(err){} //删除这个图像.
			//5. 删除句柄
			try{delete document['__youaitie'];}catch(err){}
			};
		}
		this.bind(this.gnid('_yat_n'),'click',new_i(this));
		//增加一个在页面上点击就消失的事件
		function clickme(obj){return function(){
			obj.hide(obj.gnid('_yat_tie'));
			obj.hide(obj.gnid('_yat_msg'));
			obj.hide(obj.gnid('_yat_info'));
			};
		}
		function cancelbubble(evt){
			if (evt.stopPropagation) evt.stopPropagation();
			else event.cancelBubble =true;
		}
		this.bind(document.body,"click",clickme(this));
		this.bind(this.gnid('_yat_tie'),'click',cancelbubble);
		this.bind(this.gnid('_yat_msg'),'click',cancelbubble);
		this.bind(this.gnid('_yat_info'),'click',cancelbubble);
	}
	YAT_RUNNER.prototype.showmain = function(){ //显示主页面
		//需要判断，当前页面是否是有docment的URL的
		var url = document.URL.toLowerCase();
		if ( url.substr(0,4) == 'http'){
			this.show(this.gnid('_yat_tie'));
			this.hide(this.gnid('_yat_msg'));
			this.hide(this.gnid('_yat_info'));
			//填入默认值
			this.gnid('_yat_url').value = document.URL;
			this.gnid('_yat_title').value = document.title;
			if (this.gnid('_yat_notes').value.length < 1)
				this.gnid('_yat_notes').value = this.getselect();
			this.gnid('_yat_notes').rows=2;
		}else{
			this.hide(this.gnid('_yat_tie'));
			this.hide(this.gnid('_yat_msg'));
			this.show(this.gnid('_yat_info'));
		}
	}
	YAT_RUNNER.prototype.do_i= function(){ //执行保持按钮
		function check(obj){ return function(){obj.check();} }
		if (this.img){
			document.body.removeChild(this.img); //删除这个图像.
			this.img = undefined;
		}
		//显示正在执行..
		this.gnid('_yat_msg').innerHTML = '<center><strong>正在努力收藏中...</strong></center>';
		this.hide(this.gnid('_yat_tie'));
		this.show(this.gnid('_yat_msg'));
		//开始提交数据
		this.img = new Image;
		this.img.onload=check(this); //完成加载后触发
		this.img.src=this.geturl();  //得到图片的URL
		document.body.appendChild(this.img); //添加到最后

		this.imageInterval = setInterval(check(this),250); //不间断的扫描
	}
	YAT_RUNNER.prototype.get = function(){ //执行收藏
		this.do_i();
	}
	YAT_RUNNER.prototype.check = function(){
		function close(obj){ return function(){obj.hide(obj.gnid('_yat_tie'));obj.hide(obj.gnid('_yat_msg'));};}
		if(this.img && this.img.complete){ //已经完成了
			if (this.imageInterval) clearInterval(this.imageInterval); //暂停监视器
			this.imageInterval = undefined;
			var a=this.img.width;
			if (a < 8){ //成功了
				this.gnid('_yat_msg').innerHTML = '<center><strong>页面已收藏!</strong></center>';
				setTimeout(close(this),2000);
			}else if(a < 100){  //需要重新设定书签栏.
				this.gnid('_yat_msg').innerHTML = '<center>你的书签栏工具已过期.<br/><br/>请<a href="{{httpdomain}}" target="_blank" class="yat_a"><strong>登陆系统</strong></a></center>';
			}
			//其他的不管了，一直显示收藏中就好了.除非用户再一次按钮下去.
		}
	}
	//增加输入框
	var	tie = document.createElement('div');
	tie.id = '_yat_tie';
	tie.className = 'yat';
	tie.innerHTML = ''+
'<input type="hidden" name="url" id="_yat_url">'+
'<table border="0">'+
'<tr><td class="yat-td"><input type="text" placeholder="Title" name="title" class="yat-input" id="_yat_title" title="收藏的标题"></td></tr>'+
'<tr><td class="yat-td"><select name="category" class="yat-select" id="_yat_category" title="收藏夹">{{!categorys}}</select></td></tr>'+
'<tr><td class="yat-td"><input type="text" placeholder="标签&nbsp;多个标签用逗号隔开" name="tag" class="yat-input" id="_yat_tag" title="标签 多个标签用逗号隔开" value="{{tags}}"></td></tr>'+
'<tr><td class="yat-td"><textarea placeholder="备注" name="notes" title="备注 有助于你了解收藏的内容" class="yat-textarea" id="_yat_notes"></textarea></td></tr>'+
'<tr><td class="yat-td"><input type="checkbox" name="heart" id="_yat_heart" style="float:left"><label for="_yat_heart" class="yat-label">为此收藏增加心标</label>'+
%if existed:
'&nbsp;&nbsp;您已在&nbsp;{{lasttime}}&nbsp;收藏了本页面'+
%end
%if tips:
'&nbsp;&nbsp;{{!tips}}'+
%end
'</td></tr>'+
'</table><br/>'+
'<table border="0"><tr>'+
'<td class="yat-sp"><button class="yat-btn yat-large yat-primary" id="_yat_get">收&nbsp;&nbsp;藏</button></td>'+
'<td class="yat-sp"><button class="yat-btn yat-large" id="_yat_close">关&nbsp;&nbsp;闭</button></td>'+
'<td class="yat-sp"><a href="{{httpdomain}}/my/" target="_blank" class="yat-a">我的全部收藏</a></td>'+
'<td class="yat-sp"><a href="{{httpdomain}}/newcategory/" class="yat-a" title="新建收藏夹" target="_blank" id="_yat_n">新建收藏夹</a></td>'+
'</tr></table>';
	document.body.appendChild(tie);
	//增加一个Message框
	var msg = document.createElement('div');
	msg.id = '_yat_msg';
	msg.className = 'yat-size';
	msg.innerHTML = '';
	document.body.appendChild(msg);
	//增加一个显示信息页
	var info = document.createElement('div');
	info.id = '_yat_info';
	info.className = 'yat-size';
	info.innerHTML = '<a class="yat-btn yat-btn-large" href="{{httpdomain}}/my/" target="_blank">前往我的全部收藏</a>';
	document.body.appendChild(info);

	var runner = new YAT_RUNNER();
	runner.init(); //初始化一次

	document['__youaitie'] = runner;
	runner.showmain();
})();
