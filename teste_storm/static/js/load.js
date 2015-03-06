$(document).ready(function() {
 	$("#order_index").change(function(){
 		valor = $(this).val();
 		window.location.replace("/?ord="+valor);
 	});

 	$("#order_genero").change(function(){
 		// alert($(this).val());
 		alert($(location).attr('href')); 
 		//valor = $(this).val();
 		//window.location.replace("/?ord="+valor);
 	});
   
 
});