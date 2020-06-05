import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

public class Declarative {
    private List<Integer> nMultiTable(int n) {
        return IntStream.rangeClosed(1, 9).mapToObj(x -> x * n).collect(Collectors.toList());
    }

    public Declarative() {
        final int n = 3;
        final List<Integer> threeTable = nMultiTable(3);
        String threeTableText = threeTable.stream().map(String::valueOf).collect(Collectors.joining(" "));
        System.out.println(threeTableText);
    }

    public static void main(String args[]) {
        new Declarative();
    }
}