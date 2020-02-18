
var socket = new WebSocket("ws://0.0.0.0:8000/ws");

function create_item_content(data) {
    return '<div>'+ data + '</div>'
};

socket.onmessage = function(event){
    $("#messages").append(create_item_content(event.data));
};

function send_message(event) {
    var username_input = $("#username");
    var message_input = $("#messageText");
    socket.send(username_input.val() + ": "+ message_input.val());
    message_input.val('')
    event.preventDefault();
};
