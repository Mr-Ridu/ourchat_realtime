function fetchmessages() {
    let room_name = $('#room_name').val();
    let active_user = $('#username').val();

    $.ajax({
        url: "/get_messages/" + room_name,
        method: "GET",
        success: function (response) {
            let msg = response.messages;
            $('#display').html('');
            for (i = 0; i < msg.length; i++) {
                if (msg[i].m_user === active_user) {
                    $('#display').append("<div class='text-right'> " + msg[i].messege + "<strong> :" + msg[i].m_user +  "</strong></div>");
                } else {
                    $('#display').append("<div> <img src='{% static 'img/jack.png' %}' alt='User Image'><strong>" + msg[i].m_user  +  "</strong>: " + msg[i].messege + "</div>");
                }
                
            };
        },    
    });
    setTimeout(fetchmessages, 3000);
}






$(document).ready(function () {
    fetchmessages();
    $('#send').on('click', function () {
        let username = $('#username').val();
        let room_name = $('#room_name').val();
        let message = $('#message').val();
        let csrftoken = $("input[name = csrfmiddlewaretoken]").val();

        data = { username: username, room_name: room_name, message: message, csrfmiddlewaretoken: csrftoken }
        $.ajax({
            url: "/send/",
            method: 'POST',
            data: data,
            success: function (data) {
                $("form")[0].reset();
            }
        });
    });

});