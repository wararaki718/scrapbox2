package sample

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.classification.{RandomForestClassificationModel, RandomForestClassifier}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator


object Main {
  def main(args: Array[String]): Unit = {
    val session = SparkSession.builder().master("local").appName("SampleRFC").getOrCreate()
    val df = session.read.format("csv").option("inferSchema", "true").option("header", "true").load("data/Pokemon.csv")

    df.show()

    session.sparkContext.stop()
  }
}
