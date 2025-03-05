
function signupSubmit() {
    const userName = document.getElementById("username");
    const password = document.getElementById("password");
    const wrongText = document.getElementById("wrongText");
    let data = new FormData();
    data.append("user", userName.value);
    data.append("password", password.value);

    if (password.value == "" || userName.value == ""){
        wrongText.style.visibility = "visible";
        wrongText.innerText = "Missing Field!";
        return;
    }

    fetch("/signup", {
        "method": "POST",
        "body": data,
    }).then(
        response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                wrongText.style.visibility = "visible";
                wrongText.innerText = "Username Already Taken!";
                user.value = "";
                user.style.borderColor = "red";
            }
        }
    )
}