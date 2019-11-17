package sample

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.feature.{IndexToString, StringIndexer, VectorAssembler}
import org.apache.spark.ml.classification.RandomForestClassifier

object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession
      .builder()
      .master("spark://localhost:7077")
      .appName("SamplePipeline")
      .getOrCreate()

    // download data
    val df = session.read
      .format("csv")
      .option("inferSchema", "true")
      .option("header", "true")
      .load("data/Pokemon.csv")
    df.show()

    // train test split
    val Array(trainDf, testDf) = df.randomSplit(Array(0.7, 0.3), 42)

    // select features
    val columns = Array("Total", "HP", "Attack", "Defense", "Speed", "Generation")
    val assembler = new VectorAssembler()
      .setInputCols(columns)
      .setOutputCol("features")

    // select label
    val indexer = new StringIndexer()
      .setInputCol("Type 1")
      .setOutputCol("label")
      .fit(df)

    val labelConverter = new IndexToString()
      .setInputCol("prediction")
      .setOutputCol("predictedLabel")
      .setLabels(indexer.labels)

    // model definition
    val gbtClassifier = new RandomForestClassifier()
      .setFeaturesCol("features")
      .setMaxDepth(5)
      .setSeed(42)

    // pipeline
    val pipeline = new Pipeline()
      .setStages(Array(assembler, indexer, gbtClassifier, labelConverter))

    // train
    val model = pipeline.fit(trainDf)

    // predict
    val predictDf = model.transform(testDf)
    predictDf.select("Name", "Type 1", "Type 2", "predictedLabel", "prediction").show()

    // stop spark session
    session.sparkContext.stop()
  }
}
