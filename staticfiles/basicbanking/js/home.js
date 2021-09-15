window.onload = function OnLoad(){
    document.getElementsByClassName("navbar__item")[0].style.borderBottom = "3px solid white";
    document.getElementsByClassName("navbar__item")[0].style.borderTop = "3px solid white";
}

function form__submit(){
    id = this.children[0].textContent;
    document.getElementsByTagName("form")[id-1].submit();
}

let allRows = document.getElementsByClassName("tbl__body__row");

allRows[0].addEventListener("click", form__submit);
allRows[1].addEventListener("click", form__submit);
allRows[2].addEventListener("click", form__submit);
allRows[3].addEventListener("click", form__submit);
allRows[4].addEventListener("click", form__submit);
allRows[5].addEventListener("click", form__submit);
allRows[6].addEventListener("click", form__submit);
allRows[7].addEventListener("click", form__submit);
allRows[8].addEventListener("click", form__submit);
allRows[9].addEventListener("click", form__submit);




