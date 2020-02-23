
//var stompClient = null;
var socket = null;
var username = "";


function setConnect()
{
    username = $("#username").val();
    if (username === "") {
        alert("input your name...");
        return;
    }

    socket = new SockJS("/chat")
    socket.onmessage = function(message) {receiveMessage(JSON.parse(message.data))};
    socket.onclose = function() {console.log("disconnected...")};
    socket.onopen = function() {
        $("#connect").prop("disabled", true);
        $("#username").prop("disabled", true);
        $("#conversation").show();
        sendMessage("join", username);
        console.log("connected!!");
    };
}

// dom operations
function addMessage(message) {
    $("#messages").append("<li>" + message + "</li>");
}

function addUser(user) {
    $("#userlist").append("<li id=user-" + user.id + ">" + user.name + "</li>");
}


function receiveMessage(message)
{
    switch(message.msgType) {
        case "say":
            addMessage(message.data);
            break;
        case "join":
            addUser(msg.data);
            break;
        case "users":
            message.data.forEach(function(element) { addUser(element);});
            break;
        case "left":
            $("#user-" + message.data.id).remove();
            break;
    }
}

function sendMessage(type, data)
{
    if(data !== "") {
        socket.send(JSON.stringify({type: type, data: data}));
        $("#message").val("");
        $("#message").focus();
    }
}

$(function(){
    $("form").on('submit', function (event) {
        event.preventDefault();
    });
    $("#connect").on("click", function(event){
        setConnect();
    });
    $("#send").on("click", function(event) {
        let message = username + ": " + $("#message").val();
        sendMessage("say", message);
    });
    console.log("set events.");
});
