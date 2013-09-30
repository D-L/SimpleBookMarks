<div class="modal hide" id="modal-edit">
	<div class="modal-header"><button type="button" class="close" data-dismiss="modal">×</button><h4>编辑</h4></div>
	<div class="modal-body">
		<p class="alert alert-info hide" id="successmsg-edit"></p>
		<p class="alert alert-error hide" id="errormsg-edit"></p>
		<form id="form-edit">
			<input type="text" class="span6" name="title" placeholder="帖子标题" title="收藏的标题">
			<input type="hidden" name="bookmarkid">
			<select class="span6" id="categorys-edit" name="category" title="收藏夹">
			%for catid,title in allcategorys.iteritems():
				<option value="{{catid}}">{{title}}</option>
			%end
			</select>
			<input type="text" class="span6" name="tag" data-provide="typeahead" placeholder="添加标签 多个标签之间用逗号隔开" title="添加标签 多个标签之间用逗号隔开"><br/>
			<textarea class="span6" name="notes" placeholder="添加备注" title="备注 有助于你了解收藏的内容"></textarea>
		</form>
	</div>
	<div class="modal-footer">
		<a href="javascript:void(0)" class="btn btn-primary" id="confirm-edit">确定更改</a>
		<a href="javascript:void(0)" class="btn" data-dismiss="modal">取消</a>
	</div>
</div>
