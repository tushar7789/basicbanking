let foot = document.getElementsByClassName("foot")[0];

var interval = setInterval(()=>{
    var cont = document.getElementsByClassName("main")[0];
    if(cont.scrollTop >= 0){
        foot.style.backgroundColor = "rgba(97, 100, 105, 1.0)";
    }else{
        foot.style.backgroundColor = "rgba(97, 100, 105,0.4)";
    }
}, 50);

let ele = document.getElementById("nv");

function my(){
    if (this.scrollTop > 20 ){
        ele.style.backgroundColor = "rgba(97, 100, 105, 1.0)";
    }else{
        ele.style.backgroundColor = "rgba(97, 100, 105,0.4)";
    }
}

document.getElementsByClassName("main")[0].addEventListener("scroll", my);




