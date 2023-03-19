def search_substr(subst, st):
    if subst.casefold() in st.casefold():
        return "Есть контакт!"
    else:
        return "Мимо!"
st=str(input("Введите строку"))
subst=str(input("Введите, что нужно искать"))
print(search_substr(subst,st))