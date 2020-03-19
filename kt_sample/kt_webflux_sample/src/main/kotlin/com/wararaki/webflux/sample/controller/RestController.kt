package com.wararaki.webflux.sample.controller

import org.springframework.http.MediaType
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController
import reactor.core.publisher.Flux
import java.time.Duration
import java.time.LocalDateTime
import kotlin.random.Random

@RestController
class RestController() {
    @GetMapping(value = ["/message"], produces = [MediaType.TEXT_EVENT_STREAM_VALUE])
    fun prices(): Flux<ResponseMessage> {
        return Flux.interval(Duration.ofSeconds(1)).map{ResponseMessage(getRandomMessage(), LocalDateTime.now())}
    }

    private fun getRandomMessage(x: Int = Random.nextInt(2)) = when(x) {
        1 -> "Hello!"
        else -> "World!"
    }
}
