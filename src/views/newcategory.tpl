<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>新建收藏夹-有爱帖个人版</title>
		<link href="/css/bootstrap.min.css" rel="stylesheet">
		<link rel="stylesheet" href="/css/font-awesome.min.css">
		<script type="text/javascript" charset="utf-8" src="/js/jquery.js"></script>
        <script type="text/javascript" charset="utf-8" src="/js/bootstrap.min.js"></script>
		<script type="text/javascript" charset="utf-8" src="/js/comm.min.js"></script>
	</head>
	<body>
		<div class="container">
			<ul class="nav nav-pills pull-right">
				<li class="dropdown">
					<a class="dropdown-toggle" data-target="#" data-toggle="dropdown" href="/info/">设置<i class="icon-caret-down"></i></a>
					<ul class="dropdown-menu">
						<li><a href="/my/">我的收藏</a></li>
						<li><a href="/tools/">收藏工具</a></li>
						<li class="divider"></li>
						<li><a href="/info/">设置</a></li>
						<li><a href="/signout/">退出</a></li>
					</ul>
				</li>
			</ul>
			<div class="clearfix"></div>
			<p class="alert alert-error hide" id="errormsg"></p>
			<p class="alert alert-success hide" id="successmsg"></p>
			<div class="alert alert-info" id="catform">
				<label for="title"><strong>需要新建的收藏夹名称</strong></label>
				<input type="text" class="span8" id="title" name="title" placeholder="新建收藏夹名称 不超过64个字">
				<br/>
				<button class="btn btn-primary" id="btncat">创建</button>
			</div>
			%include comm/foot
		</div>
		<script type="text/javascript">
			function success(){
				hide($("#catform"));
				showmessage($("#successmsg"),"创建成功，本页面可以关闭了哦");
			}
			function error(msg){showmessage($("#errormsg"),msg);}
            $(document).ready(
				function(){	
					$("#btncat").click(function(){
						hide($("#errormsg"));
						createcategory_i($("#title").val(),success,error);
					});
				}
			);
		</script>	
	</body>
</html>
