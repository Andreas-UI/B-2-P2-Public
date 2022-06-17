$(document).ready(function () {
    $('.pawn-preview').addClass("collapse")
});

$("#previewMarkdown").on('click', function (e) {
    var clicks = $(this).data('clicks');
    if (!clicks) {
        $('.pawn-preview').removeClass('collapse')
        $('.pawn-editor').addClass('collapse')
        $('.bi-eye-fill').toggle()
        $('.bi-eye-slash-fill').toggle()
    } else {
        $('.pawn-preview').addClass('collapse')
        $('.pawn-editor').removeClass('collapse')
        $('.bi-eye-fill').toggle()
        $('.bi-eye-slash-fill').toggle()
    }
    $(this).data("clicks", !clicks);
})

$(".pawn-bold").on("click", function (e) {
    insertMetachars("**", "**")
})

$(".pawn-italic").on("click", function (e) {
    insertMetachars("_", "_")
})

$(".pawn-heading").on("click", function (e) {
    insertMetachars("# ", "")
})

$(".pawn-blockquote").on("click", function (e) {
    insertMetachars("> ", "")
})

$(".pawn-code").on("click", function (e) {
    insertMetachars("`", "`")
})

$(".pawn-link").on("click", function (e) {
    insertMetachars("[]()", "")
})

$(".pawn-image").on("click", function (e) {
    insertMetachars("![]()", "")
})

// https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement

function insertMetachars(sStartTag, sEndTag) {
    var bDouble = arguments.length > 1,
        oMsgInput = document.pawnForm.comment,
        nSelStart = oMsgInput.selectionStart,
        nSelEnd = oMsgInput.selectionEnd,
        sOldText = oMsgInput.value;
    oMsgInput.value = sOldText.substring(0, nSelStart) + (bDouble ? sStartTag + sOldText.substring(nSelStart,
        nSelEnd) + sEndTag : sStartTag) + sOldText.substring(nSelEnd);
    oMsgInput.setSelectionRange(bDouble || nSelStart === nSelEnd ? nSelStart + sStartTag.length : nSelStart, (
        bDouble ? nSelEnd : nSelStart) + sStartTag.length);
    oMsgInput.focus();
}