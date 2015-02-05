<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8' />
        <title>{{title}}印象</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="/js/jquery.js"></script>
		<style>
			.actived { background-color: #31708f}
		</style>
    </head>
    <body>
        <div class="container-fluid">
			<h2><a href="{{prev}}"><small><span class="glyphicon glyphicon-chevron-left"></span></small></a>&nbsp;{{title}}&nbsp;<a href="{{next}}"><small><span class="glyphicon glyphicon-chevron-right"></span></small></a><div class="pull-right"><a href="/everyday/" class="btn">每日更新</a>&nbsp;<a href="/ifound/" class="btn">发布新网站</a></div></h2>
			<div class="table-responsive">
    	        <table class='table table-striped'>
        	        <tbody>
                        %for week in weeks:
						<tr>
						%for day in week:
							%if day:
								%if day[0]:
							<td><a href="{{day[0]}}"><strong><span class="badge actived">{{day[1]}}</span></strong></a></td>
								%else:
							<td><span class="badge">{{day[1]}}</span></td>
								%end
							%else:
							<td>&nbsp;</td>
							%end
						%end
                        <tr>
						%end
					</tbody>
				</table> 
			</div>
		</div>
	</body>
</html>
