package sample

import com.microsoft.ml.spark.lightgbm.{LightGBMRanker, LightGBMUtils}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{col, explode, monotonically_increasing_id, udf}


object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession.builder()
      .master("local")
      .appName("SampleLGBM")
      .getOrCreate()

    // load data
    val trainDf = session.read.format("libsvm")
      .load("data/rank.train")
      .withColumn("iid", monotonically_increasing_id())

    def createRows = udf((colValue: Int, index: Int) => List.fill(colValue)(index).toArray)

    val queryDf = session.read.format("csv")
      .option("inferSchema", true)
      .load("data/rank.train.query")
      .withColumn("index", monotonically_increasing_id())
      .withColumn("query", explode(createRows(col("_c0"), col("index"))))
      .withColumn("iid", monotonically_increasing_id())
      .drop("_c0", "index")

    val mergeDf = trainDf.join(queryDf, "iid").drop("iid")
    mergeDf.cache()

    // create features
    val featureDf = LightGBMUtils.getFeaturizer(mergeDf, "label", "_features", groupColumn = Some("query"))
      .transform(mergeDf)
      .drop("features")
      .withColumnRenamed("_features", "features")
    featureDf.cache()
//    featureDf.show()

    // train model
    val lgbmRanker = new LightGBMRanker()
      .setLabelCol("label")
      .setFeaturesCol("features")
      .setGroupCol("query")
      .setNumLeaves(5)
      .setNumIterations(10)
    val model = lgbmRanker.fit(featureDf)

    // predict
    val testDf = session.read.format("libsvm")
      .load("data/rank.test")
    val predDf = model.transform(testDf)
    predDf.show()

    // close spark session
    session.stop()
  }
}
