<!doctype html>
<html>
    <head>  
		<meta charset="utf-8">
        <title>设置信息-有爱帖个人版</title>
		<link href="/css/bootstrap.min.css" rel="stylesheet">
		<link rel="stylesheet" href="/css/font-awesome.min.css">
        <script type="text/javascript" charset="utf-8" src="/js/jquery.js"></script>
        <script type="text/javascript" charset="utf-8" src="/js/bootstrap.min.js"></script>
        <script type="text/javascript" charset="utf-8" src="/js/notify.min.js"></script>
        <script type="text/javascript" charset="utf-8" src="/js/comm.min.js"></script>
    </head>
    <body>
        <div class="container">
			<ul class="nav nav-pills pull-right">
				<li class="dropdown">
					<a class="dropdown-toggle" data-target="#" data-toggle="dropdown" href="/info/">设置<b class="caret"></b></a>
				    <ul class="dropdown-menu">
						<li><a href="/my/">我的收藏</a></li>
						<li><a href="/tools/">收藏工具</a></li>
						<li><a href="/signout/">登出</a></li>
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
				<form class="form-horizontal" id="copycatform">
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
							<button type="submit" class="btn btn-primary btn-large">设定</button>
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
			<h3 class="alert alert-info">密码修改</h3>
			<div class="alert alert-success">
			<form class="form-horizontal" id="passwordform">
				<div class="control-group">
					<label class="control-label" for="cur">当前密码</label>
					<div class="controls">
						<input type="text" placeholder="当前密码" name="cur" class="span4">
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="new">新的密码</label>
					<div class="controls">
						<input type="text" name="new" placeholder="新密码" class="span4">
					</div>
				</div>
				<div class="control-group">
			    	<div class="controls">
						<button type="submit" class="btn btn-primary btn-large">修改密码</button>
					</div>
			  </div>
			</form>
			</div>
			%include comm/foot
		</div>
		<script type="text/javascript">	
			$(document).ready(
				function(){
					$("#passwordform").submit(updatepassword);
					$("#copycatform").submit(updatecopycat);
				}
			);
		</script>
    </body>
</html>
