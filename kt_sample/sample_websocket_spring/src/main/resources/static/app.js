var stompClient = null;
var username = 'unknown';
let imageAddress = "https://sociopouch.files.wordpress.com/2019/11/d18131-1260-253752-14.jpg";

function setConnected(connected) {
    username = $("#username").val();
    // deactivate
    $("#connect").prop("disabled", connected);
    $("#username").prop("disabled", connected);

    // activate
    $("#disconnect").prop("disabled", !connected);
    $("#content").prop("disabled", !connected);
    $("#send").prop("disabled", !connected);
    if (connected) {
        $("#conversation").show();
    }
    else {
        $("#conversation").hide();
    }

    // reset
    $("#feed").html("");
}

function connect() {
    var socket = new SockJS('/chat');
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        setConnected(true);
        console.log('Connected: ' + frame);
        stompClient.subscribe('/topic/feed', function (greeting) {
            data = JSON.parse(greeting.body)
            updateFeed(data);
        });
    });
}

function disconnect() {
    if (stompClient !== null) {
        stompClient.disconnect();
    }
    setConnected(false);
    console.log("Disconnected");
}

function sendName() {
    let content = $("#content").val();
    $("#content").val("");
    stompClient.send("/app/post", {}, JSON.stringify({'name': username, 'content': content}));
}

function createMessageView(data) {
    return '<li class="media">'
            + '<img class="mr-3 custom-resize" src="' + imageAddress + '">'
            + '<div class="media-body">'
                + '<h5>' + data.name + '</h5>'
                + data.content
            + '</div>'
            + '</li>';
}

function updateFeed(data) {
    $("#feed").prepend(createMessageView(data));
}

$(function () {
    $("form").on('submit', function (e) {
        e.preventDefault();
    });
    $( "#connect" ).click(function() { connect(); });
    $( "#disconnect" ).click(function() { disconnect(); });
    $( "#send" ).click(function() { sendName(); });
});
