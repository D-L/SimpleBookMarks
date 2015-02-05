<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>感谢</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
    </head>
    <body>
        <div class="container-fluid">
			<h2>感谢分享</a><div class="pull-right"><a href="/" class="btn">回首页</a></h2>
			<div class="table-responsive">
				<div class="row">
					<div class="col-md-6 col-md-offset-3">
						<div class="alert alert-success">感谢您的分享. 2秒后我们将回到首页</div>
					</div>
				</div>
			</div>
		</div>
		<script type="text/javascript">
			$(document).ready(function(){
				setTimeout("location.href='{{homepage}}';", 3000);
			});
		</script>
	</body>
</html>
