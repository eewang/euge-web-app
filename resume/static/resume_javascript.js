/**
 * @author Eugene Wang
 */
$(document).ready(function(){
	$(".tabs li").click(function(){
		if(!$(this).hasClass("selected")){
			$(".tabs").removeClass("selected");
			$(this).addClass("selected");
		}
		var selectionId = $(this).attr("id");
		$(".content").fadeOut("slow", function(){
			$(".page").css({display:"none"});
			$(".page#" + selectionId).css({display:"block"});
			$(this).fadeIn("slow");
	});
	});
	$(".page div").click(function(){
		$(".page div p").toggleClass("hidden");
	});
	$(".header").click(function(){
		$(this).nextUntil(".header").animate(
			{height:"toggle"}, 250
		)
	})
});
