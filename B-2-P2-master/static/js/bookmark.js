$(document).ready(function () {
    $(".question_detail_bookmark_button").on('click', function (e) {
        e.preventDefault();
        const parentForm = $(this).parent()[0].getAttribute('action')
        const id = $(this).parent()[0].getAttribute('id')

        $.ajax({
            type: 'POST',
            url: parentForm,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                $("." + String(id) + "-bi-bookmark-check-fill").toggle()
                $("." + String(id) + "-bi-bookmark").toggle()
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
})