package sample;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class Main {
    public static void main(String[] args) throws SQLException {
        String host = "jdbc:mysql://127.0.0.1:3306/sample_db";

        String username = "user";
        String password = "password";
        Connection connection = DriverManager.getConnection(host, username, password);
        System.out.println(connection.getCatalog());
        System.out.println(connection.getSchema());
        System.out.println(connection.getClientInfo());
        System.out.println(connection.isClosed());
        connection.close();
        System.out.println(connection.isClosed());

        System.out.println("DONE");
    }
}
