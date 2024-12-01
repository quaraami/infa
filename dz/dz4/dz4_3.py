str = "амортизация абстракция алапеция аллегория анафора фара корректор коллектор грунт почва" 
 
for i in str.split():
    if(i.startswith("а") and i.endswith("я")):
        print(i)