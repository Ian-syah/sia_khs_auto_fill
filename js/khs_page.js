// var sem = $('#semester');
var tampil = $('#tampil');


var semId = "20201";
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