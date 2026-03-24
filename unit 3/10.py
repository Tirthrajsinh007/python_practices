fruits = ["mango","apple","grapes","watermelon"]

def add():
    inp = "gvava"
    fruits.append(inp)
add()

inp = "banana"
i = 2;
if i== None or i<0 :
    i = 1;
print(i)
def pos(i,inp):
    fruits.insert(inp,i)

pos(inp,i)
print(fruits)


def upd():
    inp = "kiwi"
    fruits[1] = inp
upd();
print(fruits)

remove_index = 2
f_name = "banana"

def remove(remove_index,f_name):
    if fruits[remove_index] == "banana":
        fruits.remove("banana")

remove(remove_index,f_name)
print(fruits)

ans = sorted(fruits,key = lambda x:x[0])
print(ans)