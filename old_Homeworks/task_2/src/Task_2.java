public class Task_2 implements Task_2_base {
    @Override
    public int subtask_1_while(int num) {
        int cifra= 1;
        int result=1;
        int bebra=1;
        while (result <= num){
            bebra=result;
            result=cifra*cifra;
            cifra=cifra+1;
        }
        return bebra;
    }

    @Override
    public int subtask_2_while(int num) {
        int p=1;
        int p2=1;
        int k=0;
        while (k!=num){
            p=p2;
            p2=2*p+6;
            k=k+1;
        }
        return p2;
    }

    @Override
    public boolean subtask_3_while(int num, int base) {
        int a=0;
        int t=base;
        while(base<num){
            a=base;
            base=base*t;
        }
        if (base==num){
            return true;
        }
        else{
            return false;
        }
    }

    @Override
    public int subtask_4_while(int start, int end) {
        int t=0;
        int k=start;
        while (k!=end){
            if (k%2>0){
                k=k-1;
                t=t+1;

            }
            else{
                if (k/end>=2){
                    k=k/2;
                    t=t+1;
                }
                else{
                    k=k-1;
                    t=t+1;
                }
            }
        }
        return t;
    }
}