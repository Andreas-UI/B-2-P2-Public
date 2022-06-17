$(document).ready(function () {
    $(".question_detail_pin_button").on('click', function (e) {
        e.preventDefault()
        const parentForm = $(this).parent()[0].getAttribute('action')
        const id = $(this).parent()[0].getAttribute('id')
        const parent = $(this).closest(".detail-description")

        $.ajax({
            type: 'POST',
            url: parentForm,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                parent.toggleClass("pinned")
                $("." + String(id) + "-bi-star").toggle()
                $("." + String(id) + "-bi-star-fill").toggle()
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
})