        $(document).ready(function() {
        //绑定下拉框change事件，当下来框改变时调用 SelectChange()方法
     $("#id_major").change(function() {
            content=$(this).find("option:selected").attr("value");
            $("#id_area option[value='迁安']").remove();
            $("#id_area").append("<option value='迁安'>迁安</option>"); 

            if(content=="医学"){
            $("#id_area option[value='迁安']").remove();
     	       };  
			});
     $("#id_ride_date").change(function() {
            content=$(this).find("option:selected").attr("value");
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            $("#id_ride_time").append("<option value='07.00'>07.00</option>"); 
            $("#id_ride_time").append("<option value='12.00'>12.00</option>"); 

            if(content=="2018.11.08"){
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            $("#id_ride_time").append("<option value='12.00'>12.00</option>"); 
            };  
            if(content=="2018.11.09"){
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            };  
         }); 
        }) 
