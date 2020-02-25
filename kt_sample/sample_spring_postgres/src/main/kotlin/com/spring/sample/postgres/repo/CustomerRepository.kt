package com.spring.sample.postgres.repo

import com.spring.sample.postgres.model.Customer
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface CustomerRepository : CrudRepository<Customer, Long> {
    fun findByLastName(lastName: String): Iterable<Customer>
}
