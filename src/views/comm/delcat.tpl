<div class="modal hide" id="modal-delcat">
	<div class="modal-header"><button type="button" class="close" data-dismiss="modal">×</button><h4>删除收藏夹</h4></div>
	<div class="modal-body">
		<p class="alert alert-error hide" id="msg-delcat"></p>
		<label>可删的空收藏夹:</label>
		<select class="span6" name="category" id="delcat-title">
		%for catid,title in emptycategorys.iteritems():
		<option value="{{catid}}">{{title}}</option>
		%end
		</select>
		<button type="submit" class="btn btn-primary" id="confirm-delcat">删除收藏夹</button>
		<a href="javascript:void(0)" class="btn" data-dismiss="modal">取消</a>
	</div>
</div>
