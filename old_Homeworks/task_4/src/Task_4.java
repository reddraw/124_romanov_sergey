import java.util.Arrays;

public class Task_4 implements Task_4_base {
    @Override
    public int[] subtask_1_arrays(int size, int a0, int d) {
        // сгенерировать и вернуть массив размера size, содержащий элементы
        // арифметической прогрессии с первым членом a0 и разностью d
        int[] bebra = new int[size];
        bebra[0] = a0;
        for(int i = 1; i < size; ++i) {
            bebra[i] = bebra[i - 1] + d;
        }
        return bebra;
    }

    @Override
    public int[] subtask_2_arrays(int size) {
        // сгенерировать и вернуть массив размера size, первые два элемента
        // которого равны единице, а каждый следующий - сумме всех предыдущих
        int[] bebra = new int[size];
        bebra[0] = 1;
        if (size > 1) {
            bebra[1] = 1;
            int k = bebra[0] + bebra[1];
            for(int i = 2; i < size; ++i, k = k + k) {
                bebra[i] = k;
            }
        }
        return bebra;
    }

    @Override
    public int[] subtask_3_arrays(int size) {
        // сгенерировать и вернуть массив размера size, содержащий первые
        // size чисел последовательности фибоначчи.
        // https://ru.wikipedia.org/wiki/Числа_Фибоначчи
        int[] bebra = new int[size];
        bebra[0] = 0;
        if (size > 1) {
            bebra[1] = 1;
            for (int i = 2; i < size; ++i) {
                bebra[i] = bebra[i - 1] + bebra[i - 2];
            }
        }
        return bebra;
    }

    @Override
    public int subtask_4_arrays(int[] data) {
        // Для данного массива вычислить максимальный элемент
        int bebra = data[0];
        for(int i = 1; i < data.length; ++i) {
            if (bebra < data[i]) {
                bebra = data[i];
            }
        }
        return bebra;
    }

    @Override
    public int subtask_5_arrays(int[] data, int k) {
        // Для данного массива вычислить максимальный элемент
        // кратный k. Гарантируется, что как минумум один такой элемент
        // в массиве есть
        int bebra = -3;
        for(int i = 1; i < data.length; ++i) {
            if (data[i] % k == 0 && data[i] > bebra) {
                bebra = data[i];
            }
        }
        return bebra;
    }

    @Override
    public int[] subtask_6_arrays(int[] arr1, int[] arr2) {
        // Даны два массива arr1, arr2.
        // Произвести слияние данных массивов в один отсортированный
        // по возрастанию массив.
        int[] bebra = new int[arr1.length + arr2.length];
        int bebra1 = arr1.length;
        int bebra2 = arr2.length;
        int j = 0;
        for(int i = 0; i < bebra1; ++i) {
            bebra[i] = arr1[i];
            ++j;
        }
        for (int k = 0; k < bebra2; ++k) {
            bebra[j] = arr2[k];
            ++j;
        }
        Arrays.sort(bebra);
        return bebra;
    }

    @Override
    public int[] subtask_7_arrays(int[] arr1, int[] arr2) {
        // Даны два отсортированных по возрастанию массива arr1, arr2.
        // Произвести слияние данных массивов в один также отсортированный
        // по возрастанию массив.
        // Используйте алгоритм, время работы которого будет пропорционально сумме
        // размеров arr1 и arr2, а не их произведению
        int[] bebra = new int[arr1.length + arr2.length];
        int bebra1 = arr1.length;
        int bebra2 = arr2.length;
        int k = 0;
        for(int i = 0; i < bebra1; ++i) {
            bebra[i] = arr1[i];
            ++k;
        }
        for (int l = 0; k < bebra2; ++l) {
            bebra[k] = arr2[l];
            ++k;
        }
        Arrays.sort(bebra);
        return bebra;
    }
}
