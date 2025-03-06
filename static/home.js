function logOut() {
    let data = new FormData();
    data.append("user", "test");

    fetch("/logout", {
        "method": "POST",
        "body": data,
    }).then(
        response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        }
    )
}

function addEvent() {
    const eventName = document.getElementById("eventName");
    const date = document.getElementById("date");
    const wrongText = document.getElementById("wrongText");
    let data = new FormData();
    data.append("eventName", eventName.value);
    data.append("date", date.value);

    if (eventName.value == "" || date.value == ""){
        wrongText.style.visibility = "visible";
        wrongText.innerText = "Empty Field!";
        return;
    }

    if (date.value.length != 10){
        wrongText.style.visibility = "visible";
        wrongText.innerText = "Incorrect date format. Ex: \"01-22-2025\"";
        return;
    }

    if (checkDate(date.value)){
        wrongText.style.visibility = "visible";
        wrongText.innerText = "Incorrect date format. Ex: \"01-22-2025\"";
        return;
    }

    wrongText.style.visibility = "hidden";

    fetch("/home", {
        "method": "POST",
        "body": data,
    }).then(
        response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        }
    )
}

/*
TODO:   check if, 0 < month < 13, and, 0 < day < 32
        depending on month, change range
        After changing event date column to hold date data type, make sure this is correct formatting
        might be easiest to just do error handling in python, and if returned not redirect, assume incorrect date inputted
*/
function checkDate(date) {
    month = date.slice(0, 2);
    day = date.slice(3, 5);
    year = date.slice(6, 10);
    if (!(/^\d+$/.test(month)) || !(/^\d+$/.test(day)) || !(/^\d+$/.test(year))){
        return true;
    }

    if (date[2] != "-" || date[5] != "-"){
        return true;
    }

    return false;

}