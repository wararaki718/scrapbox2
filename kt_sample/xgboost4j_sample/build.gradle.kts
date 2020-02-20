plugins {
    kotlin("jvm") version "1.3.61"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
    implementation("ml.dmlc:xgboost4j:0.90")
}

application {
    mainClassName = "com.xgboost.sample.MainKt"
}
