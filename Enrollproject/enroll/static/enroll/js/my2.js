        $(document).ready(function() {
        //绑定下拉框change事件，当下来框改变时调用 SelectChange()方法

     var major = $("#id_major").attr('value');
	 if (major=="医学")
	 	{
		//午餐
		  $("#id_need_lunch").append("<option value='1天'>1天/15元</option>");
		  $("#id_need_lunch").append("<option value='2天'>2天/30元</option>");
		  $("#id_need_lunch").append("<option value='不需要'>不需要</option>");
		//大巴
		  $("#id_need_bus").append("<option value='单程去'>单程去/20元</option>");
		  $("#id_need_bus").append("<option value='双程'>双程/40元(考完第三科回)</option>");
		  $("#id_need_bus").append("<option value='不需要'>不需要</option>");
		  //酒店
		  $("#id_need_dorm").append("<option value='单人间'>单人间/400元/2天+80/接送2天</option>");

		  $("#id_need_dorm").append("<option value='双人间'>双人间/200元/2天+80/接送2天</option>");
		  //天数
		  $("#id_day_dorm").append("<option value='2天'>2天</option>");

		}
	else if(major == "管联")
	   {
	   
		//午餐
		  $("#id_need_lunch").append("<option value='1天'>1天/15元</option>");
		  $("#id_need_lunch").append("<option value='不需要'>不需要</option>");
		//大巴
		  $("#id_need_bus").append("<option value='单程去'>单程去/20元</option>");
		  $("#id_need_bus").append("<option value='双程'>双程/40元</option>");
		  $("#id_need_bus").append("<option value='不需要'>不需要</option>");
		  //酒店
		  $("#id_need_dorm").append("<option value='单人间'>单人间/200元/考试时间1天+40/接送1天</option>");
		  $("#id_need_dorm").append("<option value='双人间'>双人间/100元/考试时间1天+40/接送1天</option>");
		  //天数
		  $("#id_day_dorm").append("<option value='1天'>1天</option>");
	   
	   }
	else if(major =="建工")
		{
		//午餐
		  $("#id_need_lunch").append("<option value='2天'>2天/30元</option>");
		  $("#id_need_lunch").append("<option value='不需要'>不需要</option>");
		//大巴
		  $("#id_need_bus").append("<option value='单程去'>单程去/20元</option>");
		  $("#id_need_bus").append("<option value='不需要'>不需要</option>");
		  //酒店
		  $("#id_need_dorm").append("<option value='单人间'>单人间/400元/2天+80/接送2天</option>");
		  $("#id_need_dorm").append("<option value='双人间'>双人间/200元/2天+80/接送2天</option>");
		  //天数
		  $("#id_day_dorm").append("<option value='2天'>2天</option>");
		
		}

	else
	{
		//午餐
		  $("#id_need_lunch").append("<option value='2天'>2天/30元</option>");
		  $("#id_need_lunch").append("<option value='不需要'>不需要</option>");
		//大巴
		  $("#id_need_bus").append("<option value='单程去'>单程去/20元</option>");
		  $("#id_need_bus").append("<option value='双程'>双程/40元</option>");
		  $("#id_need_bus").append("<option value='不需要'>不需要</option>");
		  //酒店
		  $("#id_need_dorm").append("<option value='单人间'>单人间/400元/2天+80/接送2天</option>");
		  $("#id_need_dorm").append("<option value='双人间'>双人间/200元/2天+80/接送2天</option>");
		  //天数
		  $("#id_day_dorm").append("<option value='2天'>2天</option>");
	
	}
	 		var money = -100 ;
			var day1 = 0 ;
			var day2 = 0 ;

			var lunch = 15 ;
			var bus1 = 20 ;
			var bus2 = 40 ;
			var single_dorm = 200;
			var double_dorm = 100;

            content1=$("#id_need_bus").find("option:selected").attr("value");
            content2=$("#id_need_dorm").find("option:selected").attr("value");
            content3=$("#id_day_dorm").find("option:selected").attr("value");
            content4=$("#id_need_lunch").find("option:selected").attr("value");


            if(content4=="1天"){
				day2 = 1; 
            };  
            if(content4=="2天"){
			 	day2 = 2;
            };  
            if(content3=="1天"){
				day1 = 1; 
            };  
            if(content3=="2天"){
			 	day1 = 2;
            };  
            if(content2=="单人间"){
				money = money + (single_dorm+40)*day1;
            };  
            if(content2=="双人间"){
				money = money + (double_dorm+40)*day1;
            };  
            if(content1=="单程去"){
				money = money+bus1;
            };  
            if(content1=="双程"){
				money = money+bus2 ;
            };  
			money = money + day2*lunch ;
			$("#id_money").attr('value',money);

     $("#id_need_lunch").change(function() {
	 		var money = -100 ;
			var day1 = 0 ;
			var day2 = 0 ;

			var lunch = 15 ;
			var bus1 = 20 ;
			var bus2 = 40 ;
			var single_dorm = 200;
			var double_dorm = 100;
            content1=$("#id_need_bus").find("option:selected").attr("value");
            content2=$("#id_need_dorm").find("option:selected").attr("value");
            content3=$("#id_day_dorm").find("option:selected").attr("value");
            content4=$("#id_need_lunch").find("option:selected").attr("value");
            if(content4=="1天"){
				day2 = 1; 
            };  
            if(content4=="2天"){
			 	day2 = 2;
            };  
            if(content3=="1天"){
				day1 = 1; 
            };  
            if(content3=="2天"){
			 	day1 = 2;
            };  
            if(content2=="单人间"){
				money = money + (single_dorm+40)*day1;
            };  
            if(content2=="双人间"){
				money = money + (double_dorm+40)*day1;
            };  
            if(content1=="单程去"){
				money = money+bus1;
            };  
            if(content1=="双程"){
				money = money+bus2 ;
            };  
			money = money + day2*lunch ;
			$("#id_money").attr('value',money);

         }); 
     $("#id_need_bus").change(function() {
	 		var money = -100 ;
			var day1 = 0 ;
			var day2 = 0 ;

			var lunch = 15 ;
			var bus1 = 20 ;
			var bus2 = 40 ;
			var single_dorm = 200;
			var double_dorm = 100;
            content1=$("#id_need_bus").find("option:selected").attr("value");
            content2=$("#id_need_dorm").find("option:selected").attr("value");
            content3=$("#id_day_dorm").find("option:selected").attr("value");
            content4=$("#id_need_lunch").find("option:selected").attr("value");
            if(content4=="1天"){
				day2 = 1; 
            };  
            if(content4=="2天"){
			 	day2 = 2;
            };  
            if(content3=="1天"){
				day1 = 1; 
            };  
            if(content3=="2天"){
			 	day1 = 2;
            };  
            if(content2=="单人间"){
				money = money + (single_dorm+40)*day1;
            };  
            if(content2=="双人间"){
				money = money + (double_dorm+40)*day1;
            };  
            if(content1=="单程去"){
				money = money+bus1;
            };  
            if(content1=="双程"){
				money = money+bus2 ;
            };  
			money = money + day2*lunch ;
			$("#id_money").attr('value',money);

         }); 
     $("#id_need_dorm").change(function() {
	 		var money = -100 ;
			var day1 = 0 ;
			var day2 = 0 ;

			var lunch = 15 ;
			var bus1 = 20 ;
			var bus2 = 40 ;
			var single_dorm = 200;
			var double_dorm = 100;

            content1=$("#id_need_bus").find("option:selected").attr("value");
            content2=$("#id_need_dorm").find("option:selected").attr("value");
            content3=$("#id_day_dorm").find("option:selected").attr("value");
            content4=$("#id_need_lunch").find("option:selected").attr("value");


            if(content4=="1天"){
				day2 = 1; 
            };  
            if(content4=="2天"){
			 	day2 = 2;
            };  
            if(content3=="1天"){
				day1 = 1; 
            };  
            if(content3=="2天"){
			 	day1 = 2;
            };  
            if(content2=="单人间"){
				money = money + (single_dorm+40)*day1;
            };  
            if(content2=="双人间"){
				money = money + (double_dorm+40)*day1;
            };  
            if(content1=="单程去"){
				money = money+bus1;
            };  
            if(content1=="双程"){
				money = money+bus2 ;
            };  
			money = money + day2*lunch ;
			$("#id_money").attr('value',money);

         }); 
     $("#id_ride_date").change(function() {
            content=$(this).find("option:selected").attr("value");
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            $("#id_ride_time").append("<option value='07.00'>07.00</option>"); 
            $("#id_ride_time").append("<option value='12.00'>12.00</option>"); 

            if(content=="3018.11.08"){
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            $("#id_ride_time").append("<option value='12.00'>12.00</option>"); 
            };  
            if(content=="3018.11.09"){
            $("#id_ride_time option[value='07.00']").remove();
            $("#id_ride_time option[value='12.00']").remove();
            };  
         }); 
        }) 
