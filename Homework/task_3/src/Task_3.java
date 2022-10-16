public class Task_3 implements Task_3_base {
    @Override
    public int subtask_1_for(int n1, int n2, int a, int b) {
        // подсчитать, сколько чисел, кратных a, но не кратных b,
        // находится между числами n1 и n2 включительно
        int t=0;
        if (n1>n2){
            while (n1-n2>=1){
                n1=n1-1;
                if ((n1%a==0) && (n1%b!=0)){
                    t=t+1;
                }
                else{
                    t=t+0;
                }
            }
        }
        else{
            while (n2-n1>=1){
                n2=n2-1;
                if ((n2%a==0) && (n2%b!=0)){
                    t=t+1;
                }
                else{
                    t=t+0;
                }
            }

        }
        return t;
    }

    @Override
    public int subtask_2_for(int num) {
        // Последовательность чисел строится следующим образом:
        // сначала идет одна единица,
        // потом две двойки,
        // потом три тройки,
        // ...
        // потом n раз число n
        // ...
        // Найти, какое число будет находиться в этой последовательности
        // на позиции num
        int t=0;
        int k=0;
        int m=1;
        while (k<num){
            k=k+m;
            t=m;
            m=m+1;
        }
        return t;
    }

    @Override
    public int subtask_3_for(int num, int d, int cnt) {
        // Дана последовательность
        // a(0) = num
        // a(n) = a(n - 1) * d + 1
        // Найти сумму первых cnt элементов последовательности
        int s=num;
        int k=1;
        int num1=num;

        while (k!=cnt){
            num1=num;
            num=num1*d+1;
            s=s+num;
            k=k+1;
        }
        return s;

    }

    @Override
    public int subtask_4_for(int n) {
        // Вычислить сумму
        // S(n) = 1 +  1 * 2 +1 * 2 * 3 + ... + n!
        // для заданного n
        // (n! - это n-факториал. Кто не знает - гуглите)
        int sum=1;
        int i=1;
        int f=n;
        int r=n;
        while (r>1){
            f=r;
            i=1;
            for(int a=1; a<=f; a++){
                i=i*a;
            }
            sum=sum+i;
            r=r-1;
        }
        return sum;
    }
}
