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
                data = response.communities
                if (Array.isArray(data)) {
                    searchResult.innerHTML = ""

                    data.forEach(function (e) {
                        searchResult.innerHTML += `
                        <div class="community-card">
        <div class="community-card-header">
            <a class="a" href="{% url 'communities_detail' pk=${e.pk} slug=${e.slug}%}">
                <img width="54" height="54" src="${e.image}">
            </a>
            <div style="gap: 5px; display: flex; flex-direction: row; align-items: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-people-fill" viewBox="0 0 16 16">
                    <path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1H7zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
                    <path fill-rule="evenodd"
                        d="M5.216 14A2.238 2.238 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.325 6.325 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1h4.216z" />
                    <path d="M4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" />
                </svg>
                ${e.member}
            </div>
        </div>
        <div class="community-card-body">
            <div>
                <a class="community-card-body-category"> ${e.category} </a>
            </div>
            <a class="a" href=${e.url}>
                <div class="community-card-body-name"> ${e.name} </div>
            </a>
            <div class="community-card-body-description"> ${e.description} </div>
        </div>
    </div>
                    `
                    })

                } else {
                    if (searchInput.value.length > 0) {
                        searchResult.innerHTML = `<div> ${data} </div>`
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