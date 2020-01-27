window.onscroll = function() {scrollFunction()};
 
function scrollFunction() {console.log(121);
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("BackTop").style.display = "block";
    } else {
        document.getElementById("BackTop").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}