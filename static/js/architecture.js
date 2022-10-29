function submitArchitecture(){
    architecture = document.getElementById("architecture").value

    url = "/architecture_info"
    data = {"architecture": architecture}

    $.ajax({
        url: url,
        type: "POST",
        async: false,
        cache: false,
        timeout: 30000,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function (response) {
            if (response.redirect) {
                window.location.href = response.redirect;
            }
        },
        error: function (response, status, error) {
            console.log("Error");
            console.log(response);
            console.log(status);
            console.log(error);
        }
    });
}