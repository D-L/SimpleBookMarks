<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>每日更新</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
		<style>
			.actived { cursor:pointer;color:#428bca;}
		</style>
    </head>
    <body>
        <div class="container-fluid">
			<h2>每日更新列表<div class="pull-right"><a href="/" class="btn">回首页</a></h2>
			<div class="table-responsive">
    	        <table class='table table-striped'>
        	        <tbody>
						%i = 0
                        %for url,st in urls:
						<tr>
							%i += 1
							%j = "%02d" % i
							<td>{{j}}.&nbsp; <a href="/url/?url={{url}}">{{url}}</a>&nbsp;最近更新于{{st}}</td>
                        <tr>
						%end
					</tbody>
				</table> 
			</div>
		</div>
	</body>
</html>
