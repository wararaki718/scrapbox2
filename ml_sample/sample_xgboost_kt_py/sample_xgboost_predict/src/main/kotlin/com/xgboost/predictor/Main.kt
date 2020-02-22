package com.xgboost.predictor

import biz.k11i.xgboost.Predictor
import biz.k11i.xgboost.util.FVec
import ml.dmlc.xgboost4j.java.DMatrix
import ml.dmlc.xgboost4j.java.XGBoost
import java.io.File
import kotlin.random.Random

fun main(args: Array<String>) {
    println("start xgboost:")

    println("load model")
    val booster = Predictor(File("../model/model.bin").inputStream())

    println("create data")
    val data = List(126){ Random.nextInt(0, 2).toDouble()}
    val features = FVec.Transformer.fromArray(data.toDoubleArray(), true)

    println("predict")
    val predicts = booster.predict(features)
    println(predicts.toList())

    println("")
    println("original package")
    println("load model")
    val booster2 = XGBoost.loadModel("../model/model.bin")

    println("load data")
    val testMat = DMatrix("../data/agaricus.txt.test")
    println(testMat.rowNum())

    println("predict2")
    val predicts2 = booster2.predict(testMat)
    println(predicts2.size)

    println("DONE")
}