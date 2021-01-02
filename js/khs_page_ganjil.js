// var sem = $('#semester');
var today = new Date();

var year = today.getFullYear();

curr_year = year.toString();

curr_year += "1"

var tampil = $('#tampil');

var semId = curr_year;
console.log(semId)


$.ajax({
    type:'post',
    url:'/pmhskhs/loaddatas',
    data:'semId='+semId,
    success:function(data)
    {
        $('#response').html(data);
         
    }
});