$(document).ready(loadPage);

function loadPage() {
    registerButtons();
    fetchImage();
};

function fetchImage() {
    let imagePromise = $.ajax({
        type: "GET",
        url: "/api"
    })
    imagePromise.done(fetchImageReady);
    imagePromise.fail(fetchImageFail);
};

function fetchImageFail(data) {
    console.log("fetching images failed!");
    console.log(data);
};

function fetchImageReady(data) {
    html = "<div class='image-container'>" +
        "<img src='/static/images/" + data + "'" +
        " alt='no image found' </img>" +
        "</br>" +
        "</div>";
    $("#container").html(html);
};

function registerButtons() {
    $("#reload").click(fetchImage);
    $("#delete").click(deleteImage);
    $("#capture").click(captureImage);
};

function captureImage(e) {
    $.ajax({
        type: "POST",
        url: "/api",
    })
        .done(function () {
            console.log("Capture page");
            fetchImage();
        });
    e.preventDefault();
};

function deleteImage(e) {
    $.ajax({
        type: "DELETE",
        url: "/api"
    })
        .done(function () {
            console.log("Images deleted")
            $("#container").html("");
        });
    e.preventDefault();
};