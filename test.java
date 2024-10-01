import java.util.Scanner;

class MinMaxArray {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements:");

        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.print("Enter array elements:");

        for (int i = 0; i < n; i++) {

            arr[i] = sc.nextInt();

        }

        int min = arr[0];

        int max = arr[0];

        for (int i = 1; i < n; i++) {
            if (arr[i] < min) {

                min = arr[i];

            }
            if (arr[i] > max) {
                max = arr[i];
            }

        }
        System.out.println("Minimum element in array is: " + min);
        System.out.println("Maximum element in array is: " + max);
    }
}