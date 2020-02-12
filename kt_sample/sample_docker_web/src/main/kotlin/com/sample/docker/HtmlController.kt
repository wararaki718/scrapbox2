package com.sample.docker

import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping

@Controller
class HtmlController {
    @GetMapping("/")
    fun sample(model: Model): String {
        model.addAttribute("title", "sample web page")
        return "sample"
    }
}
