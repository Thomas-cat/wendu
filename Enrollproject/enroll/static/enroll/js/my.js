        $(document).ready(function() {
        //绑定下拉框change事件，当下来框改变时调用 SelectChange()方法


        $("#id_ride_date").change(function() {
		
			content=$(this).find("option:selected").attr("value");

			$('#id_ride_time option').each(function(){
			this.style='display:block'}); 

            if(content=="2018.11.09"){
			$('#id_ride_time option').each(function(){
			if (this.value!='06.30')
			{
			this.style='display:none';
			} 
			});

            }
            if(content=="2018.11.08"){
			$('#id_ride_time option').each(function(){
			if (this.value=='07.00'){
			this.style='display:none';}
			});
            }

			$('#id_ride_time').trigger("chosen:updated");
		
		
		 });

        })
