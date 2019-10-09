package sample;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Sample {
    private static ObjectMapper objectMapper = new ObjectMapper();
    public static void main(String[] args) throws IOException {
        File file = new File("/Users/wararaki/projects/scrapbox2/java_sample/sample-jackson/data/user.json");
        User user = objectMapper.readValue(file, User.class);

        System.out.println(user.getInfo());
    }
}
