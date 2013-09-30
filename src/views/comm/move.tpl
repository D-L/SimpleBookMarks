<div class="modal hide" id="modal-move">
	<div class="modal-header"><button type="button" class="close" data-dismiss="modal">×</button><h4>移至其他收藏夹</h4></div>
	<div class="modal-body">
		<p class="alert alert-info hide" id="successmsg-move"></p>
		<p class="alert alert-error hide" id="errormsg-move"></p>
		<form id="form-move">
			<input type="hidden" id="bookmarkid-move" name="bookmarkid">
			<p>选择移动到的收藏夹</p>
			<select class="span6" name="category" title="收藏夹">
			%for catid,title in allcategorys.iteritems():
			<option value="{{catid}}">{{title}}</option>
			%end
			</select>
		</form>
	</div>
	<div class="modal-footer">
		<a href="javascript:void(0)" class="btn btn-primary" id="confirm-move">确定移动</a>
		<a href="javascript:void(0)" class="btn" data-dismiss="modal">取消</a>
	</div>
</div>
