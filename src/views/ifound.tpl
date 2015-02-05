<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>我在发现中...</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
		<style>
			.actived { cursor:pointer;color:#428bca;}
		</style>
    </head>
    <body>
        <div class="container-fluid">
			<h2>发现<div class="pull-right"><a href="/" class="btn">回首页</a></h2>
			<div class="table-responsive">
				<div class="row">
					<div class="col-md-6 col-md-offset-3">
					<form role="form" action="/newworld/" method="post">
					<div class="form-group">
						<label for="url">网站URL</label>
						<input type="text" class="form-control" name="url">
					</div>
					<div class="form-group">
						<label for="comment">TOKEN你懂的</label>
						<input type="text" class="form-control" name="comment">
					</div>
  					<button type="submit" class="btn btn-primary">分享发现</button>
					</form>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
