function audio(el, link)
{
    $(".selected").removeClass("selected");
    $(el).addClass('selected');
    $('#audio').attr('src', link);
    $('#play_speed').unbind('change').change(function (ev) { 
        $('#audio').prop('playbackRate', ev.target.value); 
        $('#current_speed').text(ev.target.value + 'x');
    });
}
