$(document).ready(function () {
    $("#community_search").on('input', function (e) {
        const searchInput = document.getElementById('community_search')
        const searchText = e.target.value
        const searchResult = document.getElementById('searchResult')

        if (searchResult.classList.contains('collapse')) {
            searchResult.classList.remove('collapse')
        }

        $.ajax({
            type: 'GET',
            url: '/communities/search/',
            data: {
                'searchText': searchText,
            },
            beforeSend: function () {
                $("#searching").show()
            },
            success: function (response) {
                data = response.questions
                if (Array.isArray(data)) {
                    searchResult.innerHTML = ""

                    data.forEach(function (e) {
                        searchResult.innerHTML += `
                        <div> ${e.name} </div>
                    `
                    })

                } else {
                    if (searchInput.value.length > 0) {
                        searchResult.innerHTML = `<h2> ${data} </h2>`
                    } else {
                        searchResult.classList.add('collapse')
                    }
                }
            },
            complete: function () {
                $("#searching").hide()
            },
            error: function (response) {
                console.log("error")
            }
        })
    })
})