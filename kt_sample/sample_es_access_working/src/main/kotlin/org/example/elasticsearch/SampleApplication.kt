package org.example.elasticsearch


fun main(args: Array<String>) {
    val restClientBuilder = RestClient.builder(
        HttpHost("localhost", 9200, "http")
    )
    val restHighLevelClient = RestHighLevelClient(restClientBuilder)

    restHighLevelClient.use {
        println("ES is ${restHighLevelClient.cluster().health(ClusterHealthRequest(), RequestOptions.DEFAULT).status}"
    }

    create().use { client ->
        println("ES is ${client.cluster().health(ClusterHealthRequest(), RequestOptions.DEFAULT).status}")
    }

    create(
        host = "localhost",
        port = 9200,
        https = false,
        user = null,
        password = null
    ).use { client ->
        println("ES is ${client.cluster().health(ClusterHealthRequest(), RequestOptions.DEFAULT).status}")
    }
}