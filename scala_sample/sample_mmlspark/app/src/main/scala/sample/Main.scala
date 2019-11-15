package sample

import com.microsoft.ml.spark.lightgbm.LightGBMClassifier
import org.apache.spark.ml.feature.{IndexToString, StringIndexer, VectorAssembler}
import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    // build spark session
    val session = SparkSession.builder().master("local").appName("SampleLGBM").getOrCreate()

    // load data
    val df = session.read.format("csv").option("inferSchema", "true").option("header", "true").load("data/Pokemon.csv")
    df.show()

    // choose features
    val columns = Array("Total", "HP", "Attack", "Defense", "Speed", "Generation")
    val assembler = new VectorAssembler().setInputCols(columns).setOutputCol("features")
    val featureDf = assembler.transform(df)
    featureDf.show()

    // choose label
    val indexer = new StringIndexer().setInputCol("Type 1").setOutputCol("label").fit(featureDf)
    val labelDf = indexer.transform(featureDf)
    labelDf.show()

    val labelConverter = new IndexToString().setInputCol("prediction").setOutputCol("predictedLabel").setLabels(indexer.labels)

    // train & test split
    val Array(trainingData, testData) = labelDf.randomSplit(Array(0.7, 0.3), 42)

    // modeling
    val lgbClassifier = new LightGBMClassifier()
    val model = lgbClassifier.fit(trainingData)

    val predictDf = model.transform(testData)
    labelConverter.transform(predictDf).select("Name", "Type 1", "Type 2", "predictedLabel", "prediction").show()
  }
}
