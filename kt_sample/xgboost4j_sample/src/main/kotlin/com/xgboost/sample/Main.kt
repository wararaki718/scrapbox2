package com.xgboost.sample

import ml.dmlc.xgboost4j.java.DMatrix
import ml.dmlc.xgboost4j.java.XGBoost

fun main(args: Array<String>) {
    println("start xgboost")

    val trainMat = DMatrix("src/main/resources/agaricus.txt.train")
    val testMat = DMatrix("src/main/resources/agaricus.txt.test")
    println(trainMat.rowNum())
    println(testMat.rowNum())

    val params = mapOf("eta" to 1, "max_depth" to 2, "objective" to "binary:logistic", "eval_metric" to "logloss")
    val watches = mapOf("train" to trainMat, "test" to testMat)

    println("train:")
    val nRound = 2
    val booster = XGBoost.train(trainMat, params, nRound, watches, null, null)

    println("predict:")
    val predicts = booster.predict(testMat)
    println(predicts.size)

    println("DONE")
}
