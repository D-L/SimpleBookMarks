<!doctype html>
<html>
    <head>  
		<meta charset="utf-8">
        <title>收藏工具-有爱帖个人版</title>
		<link href="/css/bootstrap.min.css" rel="stylesheet">
		<link rel="stylesheet" href="/css/font-awesome.min.css">
        <script type="text/javascript" charset="utf-8" src="/js/jquery.js"></script>
        <script type="text/javascript" charset="utf-8" src="/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
			<ul class="nav nav-pills pull-right">
				<li class="dropdown">
					<a class="dropdown-toggle" data-target="#" data-toggle="dropdown" href="/info/">设置<b class="caret"></b></a>
				    <ul class="dropdown-menu">
						<li><a href="/my/">我的收藏</a></li>
						<li class="divider"></li>
						<li><a href="/info/">设置</a></li>
						<li><a href="/signout/">登出</a></li>
					</ul>
				</li>
			</ul>
			<div class="clearfix"></div>
			<div class="alert alert-info"><h3>选择适合的收藏方式 <small>下列任意一种方式都可以</small><h3></div>
			<p><h4>方式一、书签栏工具，适用于各类浏览器</h4></p>
			<div class="alert alert-success">
				<p>拖动这个&nbsp;<a href="javascript:void(function(d){if(d['__youaitie']){d['__youaitie'].showmain();return;}b=d.createElement('script');b.id='_yat_script';b.setAttribute('charset','utf-8');b.src='{{httpdomain}}/njs/?t='+(new Date()).valueOf()+'&url='+encodeURIComponent(document.URL)+'&title='+encodeURIComponent(document.title);d.body.appendChild(b);}(document));" onclick="javascript:alert('请把这个按钮拖到你的浏览器书签栏');return false;" class="btn-primary btn btn-large" title="收藏有爱帖" style="cursor:move">+收藏有爱帖</a>&nbsp;按钮到浏览器的书签栏</p>
				<i class="icon-lightbulb icon-large"></i>&nbsp;<strong>如何使用</strong>
				<p>&nbsp;&nbsp;<strong>点击</strong>已拖到书签栏上的这个按钮</p>
				<i class="icon-lightbulb icon-large"></i>&nbsp;<strong>未发现书签栏?</strong>
				<ul>
					<li><a href="{{httpdomain}}/showyourbookmarks.html#chrome" target="_blank">显示Chrome的书签栏</a></li>
					<li><a href="{{httpdomain}}/showyourbookmarks.html#firefox" target="_blank">显示Firefox的书签栏</a></li>
					<li><a href="{{httpdomain}}/showyourbookmarks.html#safari" target="_blank">显示Safari的书签栏</a></li>
					<li><a href="{{httpdomain}}/showyourbookmarks.html#opera" target="_blank">显示Opera的书签栏</a></li>
					<li><a href="{{httpdomain}}/showyourbookmarks.html#ie" target="_blank">显示IE的书签栏</a></li>
				</ul>

				<i class="icon-lightbulb icon-large"></i>&nbsp;<strong>添加到书签栏?</strong>
				<ul>
					<li>直接将按钮拖到书签栏即可</li>
				</ul>
			</div>
			<p><h4>方式二、手工创建一个书签栏工具</h4></p>
			<div class="alert alert-success">
				<ol>
					<li>新建一个浏览器书签</li>
					<li><strong>复制下面的代码</strong>到此浏览器书签的地址项中<br/>
						<textarea class="span10" rows="2">javascript:void(function(d){if(d['__youaitie']){d['__youaitie'].showmain();return;}b=d.createElement('script');b.id='_yat_script';b.setAttribute('charset','utf-8');b.src='{{httpdomain}}/njs/?t='+(new Date()).valueOf()+'&url='+encodeURIComponent(document.URL)+'&title='+encodeURIComponent(document.title);d.body.appendChild(b);}(document));</textarea>
					</li>
					<li>完成</li>
				</ol>
				<i class="icon-lightbulb icon-large"></i>&nbsp;<strong>如何使用</strong>
				<p>&nbsp;&nbsp;<strong>点击</strong>这个新建的书签</p>
				<i class="icon-lightbulb icon-large"></i>&nbsp;<strong>手工创建实例</strong>
				<ul>
					<li><a href="{{httpdomain}}/ipad.html" target="_blank">在iPad/iPhone上创建收藏工具</a>(简单3步)</li>
				</ul>
			</div>
			%include comm/foot
		</div>
    </body>
</html>
