<!doctype html>
<html>
    <head>  
		<meta charset="utf-8">
        <title>设置信息-有爱帖个人版</title>
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
						<li><a href="/tools/">收藏工具</a></li>
					</ul>
				</li>
			</ul>
			<div class="clearfix"></div>
			<h3 class="alert alert-info">CopyCat服务设置&nbsp;<small><a href="http://112.124.44.84/service/copycat.html" target="_blank">了解CopyCat服务</a></small></h3>
			<div class="alert alert-success">
				%if enabled:
				%if appinfo:
				<h4>您当前的设定如下：</h4>
				%end
				<form class="form-horizontal" action="/setcopycat/" method="post">
					<div class="control-group">
						<label class="control-label" for="appid">APPID</label>
						<div class="controls">
							%if not appinfo:
							<input type="text" placeholder="AppID" name="appid" class="span4">
							%else:
							<input type="text" placeholder="AppID" name="appid" class="span4" value="{{appinfo[0]}}">
							%end
						</div>
					</div>
					<div class="control-group">
						<label class="control-label" for="key">Security Key</label>
						<div class="controls">
							%if not appinfo:
							<input type="text" name="key" placeholder="Security Key" class="span4">
							%else:
							<input type="text" name="key" placeholder="Security Key" class="span4" value="{{appinfo[1]}}">
							%end
						</div>
					</div>
					<div class="control-group">
						<label class="control-label" for="rooturl">入口地址</label>
						<div class="controls">
							%if not appinfo:
							<input type="text" name="rooturl" placeholder="入口地址" class="span4">
							%else:
							<input type="text" name="rooturl" placeholder="入口地址" class="span4" value="{{appinfo[2]}}">
							%end
						</div>
					</div>
					<div class="control-group">
				    	<div class="controls">
							%if appinfo:
							<button type="submit" class="btn btn-primary btn-large">重新设定</button>
							%else:
							<button type="submit" class="btn btn-primary btn-large">设定</button>
							%end
							<a href="/disablecopycat/" class="btn btn-large pull-right">停用服务</a>
						</div>
				  </div>
				</form>
				%else:
				%if msg:
					<p><strong>停用原因:</strong>&nbsp;{{msg}}</p>
				%end
				<a href="/enablecopycat/" class="btn btn-primary btn-large btn-block">启用服务</a>
				%end
			</div>
			%include comm/foot
		</div>
    </body>
</html>
