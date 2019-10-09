package sample;

public class User {
    private Integer id;
    private String name;
    private Integer age;

    public Integer getId() {
        return this.id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return this.age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getInfo() {
        StringBuilder builder = new StringBuilder();
        builder
                .append("ID: ")
                .append(this.id.toString())
                .append(", Name: ")
                .append(this.name)
                .append(", Age: ")
                .append(this.age.toString());

        return builder.toString();
    }
}
