$(document).ready(function () {
    $("#title").on('input', function (e) {
        const searchInput = document.getElementById('title')
        const searchText = e.target.value
        const searchResult = document.getElementById('searchResult')

        if (searchResult.classList.contains('collapse')) {
            searchResult.classList.remove('collapse')
        }

        $.ajax({
            type: 'GET',
            url: '/questions/search/',
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
                    <a href="${e.url}" class="a" style="padding: 5px; font-size: 1.1rem; display: flex; flex-direction: row;"> 
                    <div style="margin-right:5px;">
                    <img style="border-radius: 50%" width="32px" height="32px" src=${e.image} />
                    </div>
                    <div>
                    <div style="font-size: 0.9rem;">${e.author}, ${e.date} </div>
                    <div style="font-size: 1.1rem;">${e.title}</div>
                    </div>
                     </a>
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