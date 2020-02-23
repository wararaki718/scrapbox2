package com.sample.websocket

import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import org.springframework.web.socket.CloseStatus
import org.springframework.web.socket.TextMessage
import org.springframework.web.socket.WebSocketSession
import org.springframework.web.socket.handler.TextWebSocketHandler
import java.util.concurrent.atomic.AtomicLong

class ChatController: TextWebSocketHandler() {
    private val sessionList = HashMap<WebSocketSession, User>()
    private var uids = AtomicLong(0)

    @Throws(Exception::class)
    override fun afterConnectionClosed(session: WebSocketSession, status: CloseStatus) {
        sessionList -= session
    }

    public override fun handleTextMessage(session: WebSocketSession, message: TextMessage) {
        val json = ObjectMapper().readTree(message?.payload)

        when (json.get("type").asText()) {
            "join" -> {
                val user = User(uids.getAndIncrement(), json.get("data").asText())
                // sessionList.put(session!!, user)
                sessionList[session!!] = user

                emit(session, Message("users", sessionList.values))
                broadcastToOthers(session, Message("join", user))
            }
            "say" -> {
                broadcast(Message("say", json.get("data").asText()))
            }
        }
    }

    private fun emit(session: WebSocketSession, message: Message) = session.sendMessage(TextMessage(jacksonObjectMapper().writeValueAsString(message)))
    private fun broadcast(message: Message) = sessionList.forEach{emit(it.key, message)}
    private fun broadcastToOthers(me: WebSocketSession, message: Message) = sessionList.filterNot { it.key == me }.forEach{emit(it.key, message)}
}
