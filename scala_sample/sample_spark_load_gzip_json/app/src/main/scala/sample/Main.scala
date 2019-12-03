package sample

import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    val session = SparkSession.builder().master("local").appName("SampleLoadGzip").getOrCreate()

    val df = session.read.json("data/sample.json.gz")
    df.printSchema()
    df.show()

    session.sparkContext.stop()
  }
}
