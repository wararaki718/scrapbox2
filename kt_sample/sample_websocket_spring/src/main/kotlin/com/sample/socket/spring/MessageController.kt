package com.sample.socket.spring

import org.springframework.messaging.handler.annotation.MessageMapping
import org.springframework.messaging.handler.annotation.SendTo
import org.springframework.stereotype.Controller
import org.springframework.web.util.HtmlUtils

@Controller
class MessageController {
    @MessageMapping("/post")
    @SendTo("/topic/feed")
    fun greeting(message: Message): Message {
        Thread.sleep(100)
        val name = HtmlUtils.htmlEscape(message.name)
        val content = HtmlUtils.htmlEscape(message.content)
        return Message(name=name, content=content)
    }
}