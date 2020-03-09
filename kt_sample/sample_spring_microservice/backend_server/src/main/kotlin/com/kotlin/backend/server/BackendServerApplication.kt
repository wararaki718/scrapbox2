package com.kotlin.backend.server

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class BackendServerApplication

fun main(args: Array<String>) {
    runApplication<BackendServerApplication>(*args)
}