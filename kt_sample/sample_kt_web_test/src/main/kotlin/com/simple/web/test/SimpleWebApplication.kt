package com.simple.web.test

import org.springframework.boot.Banner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class SimpleWebApplication

fun main(args: Array<String>) {
    runApplication<SimpleWebApplication>(*args) {
        setBannerMode(Banner.Mode.OFF)
    }
}
