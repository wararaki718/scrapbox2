name := "sample_pipeline_app"

version := "0.1"

scalaVersion := "2.12.10"

val sparkVersion = "2.4.1"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-mllib" % sparkVersion
)
