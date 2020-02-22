plugins {
    kotlin("jvm") version "1.3.61"
    application
}

repositories {
    mavenCentral()
    jcenter()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
    implementation("biz.k11i:xgboost-predictor:0.3.1")
    implementation("ml.dmlc:xgboost4j:0.90")
}

application {
    mainClassName = "com.xgboost.predictor.MainKt"
}
