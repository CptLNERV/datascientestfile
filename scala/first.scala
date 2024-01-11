object First extends App{
    val word: String = "I hate Scala"
    val x: String = "scala"
    val y: String = "scala"

    println(word(0))
    println(word(1))
    println(word(3))

    println(word.length)

    println(word.slice(2,6))
    println(word.slice(7,12))
    println(x == y)
}



