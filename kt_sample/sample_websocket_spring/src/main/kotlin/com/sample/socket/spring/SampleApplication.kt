package com.sample.socket.spring

import org.springframework.boot.autoconfigure.EnableAutoConfiguration
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan

@EnableAutoConfiguration
@ComponentScan
class SampleApplication

fun main(args: Array<String>) {
    runApplication<SampleApplication>(*args)
}
