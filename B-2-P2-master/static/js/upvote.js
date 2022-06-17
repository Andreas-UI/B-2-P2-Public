$(document).ready(function () {
    $(".question_detail_upvote_button").on('click', function (e) {
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
                data = JSON.parse(response);
                if (data["code"] == "0") {
                    // console.log("0")
                    $(".comment." + String(id) + "-bi-hand-thumbs-up-fill").toggle()
                    $(".comment." + String(id) + "-bi-hand-thumbs-up").toggle()
                } else if (data["code"] == "1") {
                    // console.log("1")
                    $(".comment." + String(id) + "-bi-hand-thumbs-up-fill").toggle()
                    $(".comment." + String(id) + "-bi-hand-thumbs-up").toggle()
                    $(".comment." + String(id) + "-bi-hand-thumbs-down-fill").toggle()
                    $(".comment." + String(id) + "-bi-hand-thumbs-down").toggle()
                } else {
                    // console.log("2")
                    $(".comment." + String(id) + "-bi-hand-thumbs-up-fill").toggle()
                    $(".comment." + String(id) + "-bi-hand-thumbs-up").toggle()
                }

                $(".comment-vote-count-" + String(id)).text(data["upvote"])
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
})