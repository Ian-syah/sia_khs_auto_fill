// var sem = $('#semester');
var today = new Date();

var year = today.getFullYear() - 1;

var curr_year = year.toString();

curr_year += "2"

var tampil = $('#tampil');

var semId = curr_year;
console.log(semId)

document.querySelector("#select2-semester-container").textContent = year.toString() + " Genap"

$.ajax({
    type:'post',
    url:'/pmhskhs/loaddatas',
    data:'semId='+semId,
    success:function(data)
    {
        $('#response').html(data);
         
    }
});
