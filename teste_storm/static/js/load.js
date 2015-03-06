$(document).ready(function() {
 	$("#order_index").change(function(){
 		valor = $(this).val();
 		window.location.replace("/?ord="+valor);
 	});

 	$("#order_genero").change(function(){
 		valor = $(this).val();
 		txt = $(location).attr('href');
 		link = txt.substring(0); 
 		//window.location.replace(link+"&ord="+valor);

 	});
   
 
});