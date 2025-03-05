function logOut() {
    let data = new FormData();
    data.append("user", "test");

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