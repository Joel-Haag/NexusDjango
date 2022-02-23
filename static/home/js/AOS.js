AOS.init({
 duration: 1500
});

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})