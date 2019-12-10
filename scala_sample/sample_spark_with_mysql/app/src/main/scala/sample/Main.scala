package sample

import java.util.Properties

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
    println("connected a spark master")

//    val jdbcDf = session.read
//      .format("jdbc")
//      .option("url", "jdbc:mysql://127.0.0.1:3306/sample_db")
//      .option("dbtable", "sample")
//      .option("user", "user")
//      .option("password", "password")
//      .load()
//    println("load jdbc")


    val connectionProperties = new Properties()
    connectionProperties.put("user", "user")
    connectionProperties.put("password", "password")
    connectionProperties.put("driver", "com.mysql.jdbc.Driver")

    val connectDf = session.read.jdbc("jdbc:mysql://127.0.0.1:3306/sample_db", "sample", connectionProperties)
    println("connect a mysql")

    connectDf.show()


    // download data
//    val df = session.createDataFrame(
//      Seq(
//        new Sample("1", "sample"),
//        new Sample("2", "simple"),
//        new Sample("3", "temple"),
//        new Sample("4", "sample"),
//        new Sample("5", "simple"),
//        new Sample("6", "temple"),
//        new Sample("7", "sample"),
//        new Sample("8", "simple"),
//        new Sample("9", "temple")
//      )
//    )
//    df.show()

    // filtering
//    df.createOrReplaceTempView("test")
//    val filteredDf = session.sql("SELECT * FROM test WHERE id > 5")
//    filteredDf.show()


    // stop spark session
    session.sparkContext.stop()
  }
}
