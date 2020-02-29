package com.rest.spring.sample.controller

import com.rest.spring.sample.request.MessageRequest
import com.rest.spring.sample.response.ReplyResponse
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController

@RestController
class MessageController {
    @PostMapping("/message")
    fun message(@RequestBody message: MessageRequest): ReplyResponse {
        return ReplyResponse(name = message.name, content = "reply: " + message.content)
    }
}