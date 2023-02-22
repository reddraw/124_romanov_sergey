package task;

public enum Race {
    Orc(6, 12, 2),
    Elf(2, 9, 9),
    Dwarf(6, 10, 4),
    Halfling(1, 8, 11),
    Human(6, 7, 7);

    private int sila;
    private int zhizn;
    private int bebra;
    Race(int strength, int health, int dexterity){
        this.sila = strength;
        this.zhizn = health;
        this.bebra = dexterity;
    }
    public int strength(){
        return sila;
    }
    public int health(){
        return zhizn;
    }
    public int dexterity(){
        return bebra;
    }
}
