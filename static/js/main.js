$(document).ready(function () {
    // Add a click event handler to all elements with class "toggle-button"
    $(".toggle-button").click(function () {
        // Get the target element ID from the "data-target" attribute
        const target = $(this).data("target");
        // Toggle the visibility of the target element with a slide animation
        $("#" + target).slideToggle();
        const action = $(this).data("action");
        if (action === "show") {
            $(this).text("Show Less Answers");
            $(this).data("action", "hide");
        } else {
            $(this).text("Show More Answers");
            $(this).data("action", "show");
        }
    });

});

function showOverLay(text, id) {
    var myForm = $("#form");
    myForm.attr("action", `/answer/${id}/`);
    $("#text").text(text);
    $("#overlay").css("display", "flex");
}
function hideOverLay() {
    $("#text").text("");
    $("#overlay").css("display", "none");
}


