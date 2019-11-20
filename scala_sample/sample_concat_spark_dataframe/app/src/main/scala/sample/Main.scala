package sample

import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.monotonically_increasing_id

object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession.builder().master("local").appName("SampleLTR").getOrCreate()

    // load data
    val trainDf = session.createDataFrame(MLUtils.loadLibSVMFile(session.sparkContext, "data/rank.train"))
      .withColumn("id", monotonically_increasing_id())

    val queryDf = session.read.format("csv")
      .option("inferSchema", "true")
      .load("data/rank.train.query")
      .withColumnRenamed("_c0", "group")
      .withColumn("id", monotonically_increasing_id())
    trainDf.show()
    println(trainDf.count())
    queryDf.show()
    println(queryDf.count())

    // concatenate dfs
    val unionDf = trainDf.join(queryDf, "id").drop("id")
    unionDf.show()

    session.sparkContext.stop()
  }
}
