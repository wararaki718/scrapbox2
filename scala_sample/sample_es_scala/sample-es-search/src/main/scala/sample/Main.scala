package sample

import com.sksamuel.elastic4s.http.ElasticDsl._
import com.sksamuel.elastic4s.http.{ElasticClient, ElasticProperties}

object Main extends App {
  println("sample search code.")
  var es_host: String = "http://localhost:9200"
  var es_index: String = "bank"
  val client: ElasticClient = ElasticClient(ElasticProperties(es_host))

  var response_count = client.execute(
    catCount(es_index)
  ).await
  println(response_count.result)

  var response_alias = client.execute(
    catAliases()
  ).await
  println(response_alias.result)

  var response_search = client.execute(
    search(es_index) limit 5
  ).await
  println(response_search.result.totalHits)

  client.close()
}
