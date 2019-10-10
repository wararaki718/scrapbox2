name := "sample-es-search"

version := "0.1"

scalaVersion := "2.13.1"

val elastic4sVersion:String = "6.7.3"

libraryDependencies ++= Seq(
  "com.sksamuel.elastic4s" %% "elastic4s-core" % elastic4sVersion,
  "com.sksamuel.elastic4s" %% "elastic4s-embedded" % elastic4sVersion,
  "com.sksamuel.elastic4s" %% "elastic4s-http" % elastic4sVersion
)
