package com.spring.sample.postgres

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class DBApplication

fun main(args: Array<String>) {
    runApplication<DBApplication>(*args)
}