
class Subject {
    private var listeners: MutableList<Listener> = mutableListOf()

    fun register(listener: Listener) {
        this.listeners.add(listener)
    }

    fun unregister(listener: Listener) {
        this.listeners.remove(listener)
    }

    fun notify_listeners(event: String) {
        this.listeners.forEach({listener -> listener.update(event)})
    }
}

class Listener (_name: String, subject: Subject){
    private val name = _name
    init {
        subject.register(this)
    }

    fun update(event: String) {
        println("${this.name} recieved event ${event}")
    }
}


fun main(args: Array<String>) {
    val subject = Subject()
    val listener1 = Listener("Listener_1", subject)
    val listener2 = Listener("Listener_2", subject)

    subject.notify_listeners("message")
    
    subject.unregister(listener1)
    subject.notify_listeners("message")
}
