function callBackend(url, data_file) {
    $.ajax({
        url: url,
        type: "GET",
        async: false,
        cache: false,
        timeout: 30000,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_file),
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

function startSystem() {
    url = "/toCityAndState"
    data = null
    callBackend(url, data)
}