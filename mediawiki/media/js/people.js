$(document).ready(function(){
	$('.cross').on('click', function(){
		url = this.attributes.redirect.value;
		console.log(url);
		var ele = this
		$.ajax({
			url: url,
			success: function(res){
				flag = 1;
				$(ele).parent().parent().text("");
			}
		});
	});
});