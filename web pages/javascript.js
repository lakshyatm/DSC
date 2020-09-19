$(document).ready(function(){

  $(this).on("click",".add_more_courses",function(){

    var html = '<div class="form-group"><label for="exampleFormControlInput1">Person</label><input type="name" class="form-control" id="exampleFormControlInput1" placeholder="Name"></div>';

     $(".courses_inputs_div").append(html);


  });
});


$(function () {
  $('#datetimepicker1').datetimepicker();
});

function show(x){
  if (x==0)
  document.getElementById('split').innerHTML='<br><h4>Equally</h4><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="defaultCheck1"><label class="form-check-label" for="defaultCheck1">All</label></div><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="defaultCheck1"><label class="form-check-label" for="defaultCheck1">Person 1</label></div><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="defaultCheck1"><label class="form-check-label" for="defaultCheck1">Person 2</label></div>';
}
