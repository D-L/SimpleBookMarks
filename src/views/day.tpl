<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>{{dayid}}印象</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
		<style>
			.actived { cursor:pointer;color:#428bca;}
		</style>
    </head>
    <body>
        <div class="container-fluid">
			<h2>{{dayid}}<div class="pull-right"><a href="/" class="btn">回首页</a></h2>
			<div class="table-responsive">
    	        <table class='table table-striped'>
        	        <tbody>
                        %for count,url,tasks in data:
						<tr>
							%taskid,title,ct = tasks[-1]
							%if count == 1:
								<td><a href="{{url}}" target="_blank"><span class="label label-success">源</span></a>&nbsp;<a href="/page/{{taskid}}/">{{title}}</a></td>
							%else:
								<td><a href="{{url}}" target="_blank"><span class="label label-success">源</span></a>&nbsp;<a href="/url/?day={{dayid}}&url={{url}}">{{title}}</a></span><span class="label label-default pull-right">共{{count}}个</span></td>
							%end
                        <tr>
						%end
					</tbody>
				</table> 
			</div>
		</div>
	</body>
</html>
