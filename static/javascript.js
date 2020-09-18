
$(document).ready(function(){
  
    $(this).on("click",".add_more_courses",function(){
      
      var html = '<div class="form-group"><label for="exampleFormControlInput1">Person</label><input type="name"class="form-control" id="exampleFormControlInput1" placeholder="Name"></div>';
      
      $(".courses_inputs_div").append(html);
  
    });
  });
// $(document).ready(function(){
//   $(document).on('click', '.add_more_courses', function() {
//   // Find last software container
//     var $div = $('div[class^="cls-form-group"]:last');
//     // console.log($div);
//   //counter
//     var num = parseInt($div.prop("id").match(/\d+/g), 10) + 1;
//     console.log(num);
//   // Clone the original software container inside the click function
//     var $software_container_copy = $div.clone(true)
//       .prop('class', 'cls-form-group-'+num );
//       $('.form-group').append($software_container_copy);
//     // console.log($software_container_copy);
//   // Rename form id, for and name attributes
//     // $software_container_copy.find('label[for^="person"]:last')
//         // .attr('for', 'software-name-' + num);
//     $software_container_copy.find('input[id^="vyakti"]:last')
//         .attr('id', 'vyakti-'+num)
//         .attr('name', 'vyakti-'+num);
//  });
// });
  $(function () {
    $('#datetimepicker1').datetimepicker();
  });
  
  $(function show(x){
    if (x==0)
    document.getElementById('split').style.dispaly='block';
    else
    document.getElementById('split').style.dispaly='none';
    return;
  });
  