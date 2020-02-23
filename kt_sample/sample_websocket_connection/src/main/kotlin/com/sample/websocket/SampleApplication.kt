package com.sample.websocket

import org.springframework.boot.autoconfigure.EnableAutoConfiguration
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan

//@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan
class SampleApplication

fun main(args: Array<String>) {
    runApplication<SampleApplication>(*args)
}
