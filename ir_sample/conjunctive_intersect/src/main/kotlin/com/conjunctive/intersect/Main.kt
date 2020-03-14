package com.conjunctive.intersect


fun intersectPostings(p1: List<Int>, p2: List<Int>): List<Int> {
    var answer = mutableListOf<Int>()

    var i = 0
    var j = 0

    while(i < p1.size && j < p2.size) {
        if(p1[i] == p2[j]) {
            answer.add(p1[i])
            i++
            j++
            continue
        }

        if(p1[i] < p2[j]) {
            i++
        } else {
            j++
        }
    }

    return answer
}


fun intersectConjunctive(terms: List<String>, postings: Map<String, List<Int>>): List<Int> {
    var result = postings[terms.first()]
    var tmp = terms.slice(1 until terms.size)

    while(tmp.isNotEmpty() and result!!.isNotEmpty()) {
        result = postings[tmp.first()]?.let { intersectPostings(result!!, it) }
        tmp = tmp.slice(1 until tmp.size)
    }

    return result
}


fun main(args: Array<String>) {
    val p1 = listOf(1, 2, 3, 4, 5)
    val p2 = listOf(1, 3, 5, 7, 9)
    val p3 = listOf(2, 4, 6, 8, 10)
    val p4 = listOf(1, 5, 10, 15, 20)

    val postings = mapOf("a" to p1, "b" to p2, "c" to p3, "d" to p4)
    val terms = listOf("a", "b")

    println(intersectConjunctive(terms, postings))
}