
function loginSubmit() {
    const user = document.getElementById("users");
    const password = document.getElementById("password");
    const wrongText = document.getElementById("wrongText");
    let data = new FormData();
    data.append("user", password.value);
    data.append("password", password.value);

    if (password.value == ""){
        wrongText.style.visibility = "visible";
        wrongText.innerText = "Enter Password!";
        password.value = "";
        password.style.borderColor = "red";
        return;
    }

    fetch("/login", {
        "method": "POST",
        "body": data,
    }).then(
        response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                wrongText.style.visibility = "visible";
                wrongText.innerText = "Incorrect Password!";
                password.value = "";
                password.style.borderColor = "red";
            }
        }
    )
}