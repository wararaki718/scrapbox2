package com.simple.web.test

import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping

@Controller
class HtmlController {
    @GetMapping("/")
    fun simpleweb(model: Model): String {
        model.addAttribute("title", "Simple Web Application")
        return "simpleweb"
    }
}