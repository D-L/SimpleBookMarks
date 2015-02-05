<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>{{dayid}}日的{{title}}印象</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
		<style>
			.actived { cursor:pointer;color:#428bca;}
		</style>
    </head>
    <body>
        <div class="container-fluid">
			<h2><a href="{{url}}" target="_blank">{{title}}</a><div class="pull-right"><a href="/" class="btn">回首页</a></h2>
			<div class="table-responsive">
    	        <table class='table table-striped'>
        	        <tbody>
                        %for taskid,title,ct in data:
						<tr>
							<td><a href="/page/{{taskid}}/">{{ct}}时的印象</a></td>
                        <tr>
						%end
					</tbody>
				</table> 
			</div>
		</div>
	</body>
</html>
