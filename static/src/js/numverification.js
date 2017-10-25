$('input[name=phone]').change(function() {
   var  phone_input =  $('input[name=phone]').val();
// the api key is saved in the website object then we call it in the template and then we get its value in js
   var  api_key     =  $('#span_api_key').text();
//    console.log('input is : ' + phone_input);
   if (phone_input =="" || phone_input == undefined ){

   }
   else if ($.isNumeric(phone_input)=== false){
       show_invalid_msg();
       setTimeout(function(){  $('#validity_area').hide() }, 5000);

   }
   else{
    $.ajax({
    url: 'http://apilayer.net/api/validate?access_key=' + api_key + '&number=' + phone_input + '&format=1',
    dataType: 'jsonp',
    success: function(json) {

        if(json.valid === false){
        show_invalid_msg()
      setTimeout(function(){  $('#validity_area').hide() }, 5000);

        }
        else {
        show_valid_msg();
        setTimeout(function(){ $('#validity_area').hide();  }, 5000);

        }

    },
    error: function(dat){
//         console.log(dat);
    }
    });
   }

    function show_invalid_msg(){

        $('#validity_area').html("Not valid number");
        $('#validity_area').show();
        $('#validity_area').css("color","red");
        $('#validity_area').closest('div').addClass('has-error');

    }
    function show_valid_msg(){
        $('#validity_area').html("Valid number");
        $('#validity_area').show();
         $('#validity_area').css("color","green");
        $('#validity_area').closest('div').removeClass('has-error');
    }
//     function has_char(phone_input){
//         
//     }
 });
