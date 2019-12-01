package com.sample.apollo.wararaki;

import com.spotify.apollo.Environment;
import com.spotify.apollo.httpservice.HttpService;
import com.spotify.apollo.httpservice.LoadingException;
import com.spotify.apollo.route.Route;

public final class Main {
    public static void main(String... args) throws LoadingException {
        HttpService.boot(Main::init, "ping", args);
    }

    static void init(Environment environment) {
        environment.routingEngine()
                .registerAutoRoute(Route.sync("GET", "/ping", requestContext -> "hello, world!"));
    }
}
