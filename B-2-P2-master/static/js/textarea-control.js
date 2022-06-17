$(document).ready(function (e) {
    $("textarea").on('focusout', function (e) {
        if (!$(this).val()) {
            $(this).css("border-color", "red")
        } else {
            $(this).css("border-color", "blue")
        }
    })

    $("input").on('focusout', function (e) {
        if (!$(this).val()) {
            $(this).css("border-color", "red")
        } else {
            $(this).css("border-color", "blue")
        }
    })
})