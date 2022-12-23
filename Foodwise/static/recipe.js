$('#collapse2').hide()
$('#collapse1').hide()
$('#collapse3').hide()
$('#showimg').hide()

document.getElementById("coll1").addEventListener("click", () => {
    $('#collapse2').hide()
    $('#collapse3').hide()
    $('#collapse1').toggle()
})

document.getElementById("coll2").addEventListener("click", () => {
    $('#collapse1').hide()
    $('#collapse3').hide()
    $('#collapse2').toggle()
})

document.getElementById("coll3").addEventListener("click", () => {
    $('#collapse1').hide()
    $('#collapse2').hide()
    $('#collapse3').toggle()
})

function readURL(input) {
    $('#showimg').toggle()
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

/*
document.getElementById("photo-detection-input").addEventListener(InputEvent, () => {
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
})

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};
*/