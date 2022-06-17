$(document).ready(function () {
    $(".connect-button").on('click', function (e) {
        e.preventDefault()
        const parentForm = $(this).parent()[0].getAttribute('action')

        $.ajax({
            type: 'POST',
            url: parentForm,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                $(".connect").toggle()
                $(".disconnect").toggle()
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
})