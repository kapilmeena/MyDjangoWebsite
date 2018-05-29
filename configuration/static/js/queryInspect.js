
		$(function() {
		    $('button#calculate').bind('click', function() {
		      $.getJSON('/action/showresults', {
		        a: $('#id_formula').val()
		      }, function(data) {
		      	console.log(data);
		      	$('table').remove();
		      	if(data.error == true) {
		      		
		      		$("div#error-box").remove();
		      		$("div#example_wrapper").remove();
		      		$("div#result").append('<div id="error-box"><p>' + data.errorMessage + '</p></div>');
		      		$('#error-box').addClass("col-sm-10 alert alert-danger");	
		      	}
		      	else {
		      		$("div#error-box").remove();
		      		var formattedList = data.formatList;
		      		var textFormat = [];
		      		for (var i = 0; i < formattedList.length; i++) {
						textFormat += formattedList[i] + '\n';
					}
		      		$("#id_formula").val(textFormat);
		      		editor.setValue(document.getElementById('id_formula').value)
		      		// console.log(data.formatList);
			      	$("div#result").append('<table id="example" class="table-hover table table-striped table-bordered" style="width:100%">');
			      	$("div#example_wrapper").remove();
			      	dataSet = data.result

			      	var columnSet = data.columnlist
			      	var text = [];
					for(var i = 0; i<columnSet.length;i++){	
						text.push('{ "title":"' + columnSet[i] + '"}');
					}
					var col =  '[' + text + ']';
					var obj = JSON.parse(col);
			      	
		    		$('#example').DataTable( {
		    			data: dataSet,
		        		columns: obj,
		        		destroy: true
		        		
		      		});
	    		}
		      });
		      return false;
		    });
		  });
			
		  