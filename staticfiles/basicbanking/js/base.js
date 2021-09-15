let ele = document.getElementById("nv");

function my(){
    if (this.scrollTop > 30 ){
        console.log("change detected in base");
        ele.style.backgroundColor = "rgba(97, 100, 105, 1.0)";
    }else{
        ele.style.backgroundColor = "rgba(97, 100, 105,0.4)";
    }
}

document.getElementsByClassName("main")[0].addEventListener("scroll", my);



