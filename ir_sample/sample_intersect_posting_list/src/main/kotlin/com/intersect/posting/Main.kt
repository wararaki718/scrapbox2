package com.intersect.posting

fun intersect(p1: List<Int>, p2: List<Int>): List<Int> {
    var answer = mutableListOf<Int>()

    var i = 0
    var j = 0

    while(i < p1.size && j < p2.size) {
        if(p1[i] == p2[j]) {
            answer.add(p1[i])
            i++
            j++
        } else {
            if(p1[i] < p2[j]) {
                i++
            } else {
                j++
            }
        }
    }

    return answer
}


fun main(args: Array<String>) {
    val p1 = listOf(1, 2, 3, 4, 5)
    val p2 = listOf(1, 3, 5, 7, 9)

    println(p1)
    println(p2)

    val result = intersect(p1, p2)
    println(result)
}