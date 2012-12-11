function go_play() {
    var url = $('#feed_url').val();
    document.location='/play/'+encodeURIComponent(url);
}

$(function () {
    $('#submit').click(go_play);
});

