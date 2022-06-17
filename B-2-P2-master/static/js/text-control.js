$(document).ready(function () {
    $('.text-control').on("input", function (e) {
        // console.log(e.target.value);
        this.style.height = "";
        this.style.height = this.scrollHeight + "px"
    })

    $('.pawn-editor').on("input", function (e) {
        // console.log(e.target.value);
        this.style.height = "";
        this.style.height = this.scrollHeight + "px"
    })

    $('.pawn-editor').height( $(".pawn-editor")[0].scrollHeight );
})