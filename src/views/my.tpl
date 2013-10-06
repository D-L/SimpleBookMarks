<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>我的收藏-有爱帖个人版</title>
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
				%if disabled:
				<li><a href="/info/" title="CopyCat服务停用中" class="badge badge-warning"><i class="icon-bell"></i></a></li>
				%end
				<li class="dropdown">
					<a class="dropdown-toggle" data-target="#" data-toggle="dropdown" href="/info/">设置<i class="icon-caret-down"></i></a>
					<ul class="dropdown-menu">
						<li><a href="/tools/">收藏工具</a></li>
						<li class="divider"></li>
						<li><a href="javascript:void(0)" onclick="my_show_import()">导入浏览器导出的HTML收藏</a></li>
						<li><a href="/export/" target="_blank">导出收藏为HTML文件</a></li>
						<li class="divider"></li>
						<li><a href="/info/">设置</a></li>
						<li><a href="/signout/">退出</a></li>
					</ul>
				</li>
			</ul>
			<div class="clearfix"></div>
			%if updatemsg:
				<h4 class="alert alert-danger">{{updatemsg}}<br/><a href="https://www.youaitie.net/opensource.html" class="btn btn-primary" target="_blank">立即更新</a></h4>
			%end
			%if categorys:
			<div class="alert alert-info">
				<strong>我的收藏夹</strong>&nbsp;<span class="uc" onclick="my_show_newcat()" title="创建新的收藏夹"><i class="icon-plus-sign"></i></span>
				%if len(emptycategorys) > 0:
				&nbsp;<a href="javascript:void(0)" onclick="my_show_delcat()" title="删除收藏夹"><i class="icon-minus-sign"></i></a>
				%end
				%if len(categorys) > 1:
				<button class="close" data-dismiss="alert" id="more">
					<i class="icon-chevron-down"></i>
				</button>
				%end
			</div>
			<table class="table" id="bookmark">
				<tbody>
					%for category in categorys:
					<tr>
						%for url,title,count in category:
						%if url:
						<td style="border-top:none">
							<a href="{{!url}}">{{title}}({{count}})</a>
						</td>
						%else:
						<td style="border-top:none">&nbsp;</td>
						%end
						%end
					</tr>
					%end
				</tbody>
			</table>
			%end
			%if len(bookmarks) < 1:
				<center><h3 class="alert alert-success">您还没有开始收藏呢，<a href="/tools/">立即开始</a>你的收藏之旅吧</h3></center>
			%else: #含有bookmarks的
<div class="alert alert-success">
	%if curcatinfo[0]:
		<a href="/my/"><strong>我的全部收藏</strong></a>&nbsp;<i class="icon-double-angle-right"></i>&nbsp;<strong>{{curcatinfo[0]}}({{curcatinfo[1]}})</strong>
	%else:
		<strong>我的全部收藏({{curcatinfo[1]}})</strong>
	%end
</div>
<table class="table table-striped table-bordered"><tbody>
	%for aid,url,title,_,_,notes,tt,thistags,isheart,thisarchive in bookmarks:
		<tr class="op">
			<td class="bulk hide">
				<span class="uc"><i class="icon-large icon-check-empty" bid="{{aid}}"></i></span>
			</td>
			<td>
				<span>
					<!-- {{isheart}} -->
					%if isheart == 1:
						<span id="heartico_{{aid}}">
					%else:
						<span id="heartico_{{aid}}" class="hide">
					%end
							<a href="/myheart/"><i class="icon-heart ico" title="喜爱的"></i></a>
						</span>
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
					%if isheart == 1:
						<span class="badge badge-success uc" title="取消喜爱" onclick="heart('{{aid}}')"><i class="icon-heart-empty" id="heart_{{aid}}"></i></span>
					%else:
						<span class="badge badge-success uc" title="加喜爱" onclick="heart('{{aid}}')"><i class="icon-heart" id="heart_{{aid}}"></i></span>
					%end
						<span class="badge badge-success uc" onclick="my_show_edit('{{aid}}')" title="编辑"><i class="icon-edit"></i></span>
						<span class="badge badge-success uc" onclick="my_show_del('{{aid}}')" title="删除"><i class="icon-trash"></i></span>
					%if thisarchive == 3:
						<a class="badge badge-success uc" title="看快照" href="/vss/{{aid}}/" target="_blank"><i class="icon-picture"></i></a>
					%elif thisarchive ==1:
						<span class="badge badge-success uc" title="正在快照中..."><i class="icon-refresh"></i></span>
					%elif thisarchive ==2:
						<span class="badge badge-success uc" title="准备快照中..."><i class="icon-refresh"></i></span>
					%elif thisarchive ==0:
						<span class="badge badge-success uc" title="拍个快照" onclick="snapshot('{{aid}}')"><i class="icon-camera" id="ss_{{aid}}"></i></span>
					%elif thisarchive == -1: #提示用户这里可以升级的
						<a class="badge uc" title="启用收藏快照，来个完美的页面快照吧" href="/info/"><i class="icon-camera"></i></a>
					%end
				</div>
			</td>
		</tr>
	%end
</tbody></table>
<ul class="pager pull-left">
	%curpage,pagecount,prevurl,nexturl = pages	
	%if curpage > 1:
		<li class=""><a href="{{!prevurl}}" id="prevlink">&larr;前页</a></li>
	%else:
		<li class="disabled"><a href="javascript:void(0)">&larr;前页</a></li>
	%end
	%if pagecount > 0:
		<span class="label label-info"><strong>{{curpage}}/{{pagecount}}</strong></span>
	%end
	%if curpage < pagecount:
		<li class=""><a href="{{!nexturl}}" id="nextlink">后页&rarr;</a></li>
	%else:
		<li class="disabled"><a href="javascript:void(0)">后页&rarr;</a></li>
	%end
</ul>
<ul class="pager pull-right">
	<li><a href="javascript:void(0)" id="bulkop">批量操作</a></li>
</ul>
<ul class="pager pull-right op hide">
	<li><a href="javascript:void(0)" id="bulkselect">全选</a></li>
	<li><a href="javascript:void(0)" id="bulkheart" title="加喜爱"><i class="icon-heart icon-large"></i></a></li>
	<li><a href="javascript:void(0)" id="bulkmove" title="改变收藏的收藏夹"><i class="icon-move icon-large"></i></a></li>
	<li><a href="javascript:void(0)" id="bulkdel" title="删除收藏"><i class="icon-trash icon-large"></i></a></li>
</ul>
<script type="text/javascript">
	var bulkoptunner = new Turnner(
			function(){
				$.each($("tr.op div"),function(i,v){hide($(v));}); //隐藏了曾经存在的状态.
				show($('ul.op')); 
				//打开第一项
				show($('tr.op > td.bulk')); 
				updateStatus('bulk',1); //更新当前状态为bulk操作，这样鼠标进入的时候不会显示每项的OP了
				$("#bulkop").text("关闭批量操作");
			},
			function(){
				hide($('ul.op')); 
				hide($('tr.op > td.bulk')); 
				updateStatus('bulk',0); //更新当前状态
				$("#bulkop").text("批量操作");
			}
		);
		var bulkselecttunner = new Turnner(
			function(){
				$("#bulkselect").text("全不选");
				$.each($("tr.op>td.bulk i"),function(i,v){$(v).removeClass('icon-check-empty').addClass('icon-check');});
			},
			function(){
				$("#bulkselect").text("全选");
				$.each($("tr.op>td.bulk i"),function(i,v){$(v).removeClass('icon-check').addClass('icon-check-empty');});
			}
		);
		%if len(categorys) > 1: #类目多的
		var moreturnner = new Turnner(
			function(){
				hide($("#bookmark tr"));
				show($("#bookmark tr:first"));
				$("#more i").removeClass('icon-chevron-up').addClass('icon-chevron-down');
				$("#more").attr('title','显示全部收藏夹');
			},
			function(){
				show($("#bookmark tr"));
				$("#more i").removeClass('icon-chevron-down').addClass('icon-chevron-up');
				$("#more").attr('title','收起');
			}
		);
		%end
		var opt = { //用来提示Tag
			source : [{{!tags}}],items : 5,
			matcher : ahead_matcher, sorter : ahead_sorter, updater : ahead_updater
		};
           $(document).ready(
			function(){
				//批量操作菜单
				$("#bulkop").click(function(){bulkoptunner.turn();});
				$("#bulkselect").click(function(){bulkselecttunner.turn();});

				$("tr.op").click(
					function(evt){
						if (!getStatus('bulk')) return;
						$(this).find('td.bulk i').click();
				}); 
				$("tr.op > td.bulk i").click(function(evt){
					evt.stopPropagation(); //禁止向上冒泡了
					var o = $(this);
					if (o.hasClass('icon-check-empty')) o.removeClass('icon-check-empty').addClass('icon-check');
					else o.removeClass('icon-check').addClass('icon-check-empty');
				});
				//-目录
				$("#confirm-newcat").click(my_confirm_newcat);
				$("#confirm-delcat").click(my_confirm_delcat);

				%if len(categorys) > 1: #more目录
				moreturnner.turn();
				$("#more").click(function(){moreturnner.turn();});
				%end

				//-收藏条目细节
				$("tr.op").mouseover(function(e){if(!getStatus('bulk')){var t = $(e.target);if (!t.children('div').hasClass('hide')) return;$("tr.op").find('div').addClass('hide');t.children('div').removeClass('hide');}});
				//删除用的
				$("#confirm-del").click(my_confirm_del);
				$("#confirm-bulkdel").click(my_confirm_bulkdel);
				$("#bulkdel").click(my_show_bulkdel);

				//编辑部分
				$('#form-edit > input[name="tag"]').typeahead(opt);
				$("#form-edit> textarea").focus(function(e){e.target.rows=8;});
				$("#confirm-edit").click(my_confirm_edit);
				//手动增加部分
				$('#form-add > input[name="tag"]').typeahead(opt);
				$('#url-add').blur(try_to_get_title);
				$('#confirm-add').click(my_confirm_add);

				//移动
				$("#bulkmove").click(my_show_move);
				$("#confirm-move").click(my_confirm_move);
				//批量喜爱/不喜爱
				$("#bulkheart").click(bulkheart);
			}
		);
	</script>
			%end
		<div class="clearfix"></div>
		%include comm/foot
		</div>
		%if len(bookmarks) > 0:
			%include comm/edit allcategorys=allcategorys
			%include comm/del
			%include comm/wait
			%include comm/bulkdel
			%include comm/newcat
			%if len(emptycategorys) > 0:
				%include comm/delcat emptycategorys=emptycategorys
			%end
			%include comm/move allcategorys=allcategorys
		%end
		%include comm/import
	</body>
</html>
