var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("mainNav").style.top = "100";
  } else {
    document.getElementById("mainNav").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}