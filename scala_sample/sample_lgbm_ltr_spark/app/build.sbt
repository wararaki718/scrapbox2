name := "app"

version := "0.1"

scalaVersion := "2.11.12"


val sparkVersion = "2.4.4"

resolvers += "MMLSpark Repo" at "https://mmlspark.azureedge.net/maven"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-mllib" % sparkVersion,
  "com.microsoft.ml.spark" %% "mmlspark" % "1.0.0-rc1"
)
