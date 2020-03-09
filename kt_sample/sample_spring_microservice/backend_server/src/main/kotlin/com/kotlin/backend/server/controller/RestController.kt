package com.kotlin.backend.server.controller

import com.kotlin.backend.server.controller.request.MessageRequest
import com.kotlin.backend.server.controller.response.ReplyResponse
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController
import java.time.LocalDateTime

@RestController
class RestController {
    @PostMapping("/message")
    fun message(@RequestBody message: MessageRequest): ReplyResponse {
        println(message.requestTime)
        val responseTime = LocalDateTime.now().toString()
        return ReplyResponse(content = "reply: " + message.content, responseTime = responseTime)
    }
}