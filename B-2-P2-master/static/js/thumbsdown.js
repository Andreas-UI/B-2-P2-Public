$(document).ready(function () {
    $(".question_detail_thumbsdown_button").on('click', function (e) {
        e.preventDefault()
        const parentForm = $(this).parent()[0].getAttribute('action')
        const id = $(this).parent()[0].getAttribute('id')

        $.ajax({
            type: 'POST',
            url: parentForm,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                // console.log(response)
                data = JSON.parse(response);
                if (data["code"] == "0") {
                    // console.log("0")
                    $("." + String(id) + "-bi-hand-thumbs-down-fill").toggle()
                    $("." + String(id) + "-bi-hand-thumbs-down").toggle()
                } else if (data["code"] == "1") {
                    // console.log("1")
                    $("." + String(id) + "-bi-hand-thumbs-down-fill").toggle()
                    $("." + String(id) + "-bi-hand-thumbs-down").toggle()
                    $("." + String(id) + "-bi-hand-thumbs-up-fill").toggle()
                    $("." + String(id) + "-bi-hand-thumbs-up").toggle()
                } else {
                    // console.log("2")
                    $("." + String(id) + "-bi-hand-thumbs-down-fill").toggle()
                    $("." + String(id) + "-bi-hand-thumbs-down").toggle()
                }

                $(".thumbsup-count-" + String(id)).text(data["thumbsup"])
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
})