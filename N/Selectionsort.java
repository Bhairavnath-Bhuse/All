
import java.util.Arrays;
public class Selectionsort{
    public static void selectionsort(int arr[]){
        for(int i=0; i<arr.length; i++){
            int min=i;
            for(int j=i+1; j<arr.length-1; j++){
                if(arr[j]<arr[min]){
                    min = j;
                }
            }
            //swap
            int temp = arr[min];   
            arr[min] = arr[i];  
            arr[i] = temp;  
        }
    }
    public static void main(String args[]){
        int arr[] = {12, 25, 12, 22, 64};
        selectionsort(arr);
        System.out.println("Sorted array:" +  Arrays.toString(arr));
       


    }
}