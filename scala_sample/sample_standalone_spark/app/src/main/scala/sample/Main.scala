package sample

import org.apache.spark.sql.SparkSession

case class Sample(id: String, name: String)

object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession
      .builder()
      .master("spark://localhost:7077")
      .appName("SamplePipeline")
      .getOrCreate()

    // download data
    val df = session.createDataFrame(
      Seq(
        new Sample("1", "sample"),
        new Sample("2", "simple"),
        new Sample("3", "temple"),
        new Sample("4", "sample"),
        new Sample("5", "simple"),
        new Sample("6", "temple"),
        new Sample("7", "sample"),
        new Sample("8", "simple"),
        new Sample("9", "temple")
      )
    )
    df.show()

    // filtering
    df.createOrReplaceTempView("test")
    val filteredDf = session.sql("SELECT * FROM test WHERE id > 5")
    filteredDf.show()

    // stop spark session
    session.sparkContext.stop()
  }
}
