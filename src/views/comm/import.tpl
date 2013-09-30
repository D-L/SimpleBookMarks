<div class="modal hide" id="modal-import">
	<div class="modal-header"><button type="button" class="close" data-dismiss="modal">×</button><h4>导入</h4></div>
	<div class="modal-body">
		<div class="alert alert-info hide" id="successmsg-import"></div>
		<div class="alert alert-error hide" id="errormsg-import"></div>
		<form id="importform" method="POST" action="/import/" enctype="multipart/form-data">
			<label for="name"><strong>选择需要导入的HTML文件</strong><a href="/exportbookmark.html" title="HTML文件?这是什么?" target="_blank" class="tt"><i class="icon-question-sign"></i></a></label>
			<div class="alert alert-success">
			<input type="file" class="span6" name="name" accept="text/html" />
			</div>
			<br/>
			<button type="submit" class="btn btn-primary">导入</button>
		</form>
	</div>
</div>
