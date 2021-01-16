// var sem = $('#semester');

var today = new Date();

// Get Current Month
var curr_month = today.getMonth()

// Get Current Year
var year = today.getFullYear();

// Convert year from number to string
var curr_year = year.toString();

// Append 1 to the year which mean Semester Ganjil
curr_year += "1"

var tampil = $('#tampil');

var semId = curr_year;
console.log(semId)

document.querySelector("#select2-semester-container").textContent = year.toString() + " Ganjil"
 

$.ajax({
    type:'post',
    url:'/pmhskhs/loaddatas',
    data:'semId='+semId,
    success:function(data)
    {
        $('#response').html(data);
         
    }
});
