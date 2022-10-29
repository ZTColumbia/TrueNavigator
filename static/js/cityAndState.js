function submitCountryStateCity(){
    country = document.getElementById("country").value
    state = document.getElementById("state").value
    city = document.getElementById("city").value


    url = "/address_info"
    data = {"country": country, "state": state, "city": city}

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

function callGPT() {
    prompt = "Give me 5 suggested cities and states for living."
    data = {"prompt": prompt}
        $.ajax({
        url: "/callGPT",
        type: "POST",
        async: false,
        cache: false,
        timeout: 30000,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function (response) {
            console.log(response)
        },
        error: function (response, status, error) {
            console.log("Error");
            console.log(response);
            console.log(status);
            console.log(error);
        }
    });
}

$(document).ready(function () {
});