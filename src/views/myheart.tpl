<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>我的喜爱收藏-有爱帖个人版</title>
		<link href="/css/bootstrap.min.css" rel="stylesheet">
		<link rel="stylesheet" href="/css/font-awesome.min.css">
		<script type="text/javascript" charset="utf-8" src="/js/jquery.js"></script>
		<script type="text/javascript" charset="utf-8" src="/js/bootstrap.min.js"></script>
		<script type="text/javascript" charset="utf-8" src="/js/comm.min.js"></script>
		<style>
			span.uc{cursor:pointer;}
			.title{max-width:780px;display:inline-block;overflow:hidden; text-overflow:ellipsis; white-space:nowrap;word-break:keep-all;}
			td.bulk i{color:#cc4036}
			.ico{color:#cc4036}
			.tt{font-size:12px;color:gray}
			pre {
				margin : 1px;
				white-space: pre-wrap;       /* css-3 */
				white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
				white-space: -pre-wrap;      /* Opera 4-6 */
				white-space: -o-pre-wrap;    /* Opera 7 */
				word-wrap: break-all;       /* Internet Explorer 5.5+ */
			}
		</style>
	</head>
	<body>
		<div class="container">
			<ul class="nav nav-pills pull-right">
				<li class="dropdown">
					<a class="dropdown-toggle" data-target="#" data-toggle="dropdown" href="/info/">设置<i class="icon-caret-down"></i></a>
				    <ul class="dropdown-menu">
						<li><a href="/tools/">收藏工具</a></li>
						<li class="divider"></li>
						<li><a href="/info/">设置</a></li>
						<li><a href="/signout/">退出</a></li>
					</ul>
				</li>
			</ul>
			<div class="clearfix"></div>
			%if len(bookmarks) < 1:
				<center><h3 class="alert alert-success">您还没有<i class="icon-heart ico"></i>的收藏呢，慢慢的就会遇到啦</h3></center>
			%else:
			<div class="alert alert-success"><strong><a href="/my/">全部收藏</a></strong>&nbsp;<i class="icon-double-angle-right"></i>&nbsp;<strong>加<i class="icon-heart ico"></i>的收藏(<span id="count">{{count}}</span>)</strong></div>
			<table class="table table-striped table-bordered"><tbody>
				%for aid,url,title,_,_,notes,tt,thistags,isheart,thisarchive in bookmarks:
				<tr class="op" id="tr_{{aid}}">
					<td>
					<span>
						<span><i class="icon-heart ico" title="喜爱的"></i></span>
						<a href="{{!url}}" target="_blank" title="{{title}}" class="title" id="title_{{aid}}">{{title}}</a>
						<span class="pull-right tt">{{tt}}&nbsp;收藏</span>
					</span>
					%if notes:
						<pre>&nbsp;&nbsp;{{!notes}}</pre>
					%else:
						<br/>
					%end
					%if thistags:
						<span>
						%for t,u in thistags:
							<a href="{{!u}}" class="label">{{t}}</a>
						%end
						</span>
					%end
					<div class="hide">
						<span class="badge badge-success uc" title="取消喜爱" onclick="cancelheart('{{aid}}')"><i class="icon-heart-empty"></i></span>

						<span class="badge badge-success uc" onclick="my_show_edit('{{aid}}')" title="编辑"><i class="icon-edit"></i></span>
						<span class="badge badge-success uc" onclick="my_show_del('{{aid}}')" title="删除"><i class="icon-trash"></i></span>
						%if thisarchive == 2:
						<a class="badge badge-success uc" title="看快照" href="/vss/{{aid}}/" target="_blank"><i class="icon-picture"></i></a>
						%elif thisarchive ==1:
						<span class="badge badge-success uc" title="正在快照中..."><i class="icon-refresh"></i></span>
						%elif thisarchive ==0:
						<span class="badge badge-success uc" title="拍个快照" onclick="snapshot('{{aid}}')"><i class="icon-camera" id="ss_{{aid}}"></i></span>
						%elif thisarchive == -1: #提示用户这里可以升级的
						<a class="badge uc" title="启用收藏快照，给此收藏拍个快照吧" href="/info/"><i class="icon-camera"></i></a>
						%end
					</div>
				</td></tr>
				%end
			</tbody></table>
			%end
			<div class="clearfix"></div>
			%include comm/foot
		</div>
		%if len(bookmarks) > 0:
		<script type="text/javascript">
			var opt = { //用来提示Tag
				source : [{{!tags}}],items : 5,
				matcher : ahead_matcher, sorter : ahead_sorter, updater : ahead_updater
			};
            $(document).ready(
				function(){
					//-目录
					$("#confirm-newcat").click(my_confirm_newcat);
					$("#confirm-delcat").click(my_confirm_delcat);

					//-收藏条目细节
					$("tr.op").mouseover(function(e){if(!getStatus('bulk')){var t = $(e.target);if (!t.children('div').hasClass('hide')) return;$("tr.op").find('div').addClass('hide');t.children('div').removeClass('hide');}});

					//删除用的
					$("#confirm-del").click(my_confirm_del);
					//编辑部分
					$('#form-edit> input[name="tag"]').typeahead(opt);
					$("#form-edit> textarea").focus(function(e){e.target.rows=8;});
					$("#confirm-edit").click(my_confirm_edit);
				}
			);
		</script>	
		%include comm/edit allcategorys=allcategorys
		%include comm/del
		%end
	</body>
</html>
