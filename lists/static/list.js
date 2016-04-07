

$(document).ready(function(){//确保执行脚本之前完全加载了页面
	$('input').on('keypress',function(){//输入内容才才隐藏错误提示信息
		$('.has-error').hide();
	});
	
});