package com.xgboost.predictor.sample

import biz.k11i.xgboost.Predictor
import biz.k11i.xgboost.util.FVec
import ml.dmlc.xgboost4j.java.DMatrix
import ml.dmlc.xgboost4j.java.XGBoost
import java.io.File
import kotlin.random.Random

fun main(args: Array<String>) {
    println("start xgboost:")

    val trainMat = DMatrix("src/main/resources/agaricus.txt.train")
    val testMat = DMatrix("src/main/resources/agaricus.txt.test")
    println(trainMat.rowNum())
    println(testMat.rowNum())

    val params = mapOf("eta" to 1, "max_depth" to 2, "objective" to "binary:logistic", "eval_metric" to "logloss")
    val watches = mapOf("train" to trainMat, "test" to testMat)

    println("train:")
    val nRound = 2
    val booster = XGBoost.train(trainMat, params, nRound, watches, null, null)

    booster.saveModel("src/main/resources/model.bin")

    println("predict original:")
    val model = XGBoost.loadModel("src/main/resources/model.bin")
    val predicts = model.predict(testMat)
    println(predicts.size)


    println("predict predictor:")
    val predictor = Predictor(File("src/main/resources/model.bin").inputStream())
    val values = List(126){ Random.nextInt(0, 2).toDouble()}
    val vec = FVec.Transformer.fromArray(values.toDoubleArray(), true)
    val predicts2 = predictor.predict(vec)
    println(predicts2.toList())
}