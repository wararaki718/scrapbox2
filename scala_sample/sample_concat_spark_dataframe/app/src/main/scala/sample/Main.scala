package sample

import com.microsoft.ml.spark.lightgbm.{LightGBMClassifier, LightGBMRanker}
import org.apache.spark.ml.feature.{IndexToString, StringIndexer, VectorAssembler}
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.monotonically_increasing_id

object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession.builder().master("local").appName("SampleLTR").getOrCreate()

    // load data
    val trainDf = session.createDataFrame(MLUtils.loadLibSVMFile(session.sparkContext, "data/rank.train")).withColumn("id", monotonically_increasing_id())
    val testDf = session.createDataFrame(MLUtils.loadLibSVMFile(session.sparkContext, "data/rank.test"))
    val queryDf = session.read.format("csv")
      .option("inferSchema", "true")
      .load("data/rank.train.query")
      .withColumnRenamed("_c0", "group")
      .withColumn("id", monotonically_increasing_id())
    trainDf.show()
    testDf.show()
    queryDf.show()

    val unionDf = trainDf.join(queryDf, "id").drop("id")
    unionDf.show()

    session.sparkContext.stop()
  }
}
