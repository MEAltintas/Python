name = "Imaginary Irene jhajd Irene jasdjas Irene"

print(name.count("I"))
print("Irreverent Irises in Islington".count("I"))
print(name.count("Irene"))
print(name.find("Irene"))
print("A completely different string".find("Irene"))
name.replace("I","A")
print("hello world".split(" "))
print("Annem ile pazara gittim ve pazardan elma, armut, ayva ve çilek aldım".split(","))
print("Annem ile pazara gittim ve pazardan elma, armut, ayva ve çilek aldım".split("ve"))
print("Annem ile pazara gittim  pazardan elma, armut, ayva ve çilek aldım".split("ve"))


txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") 

txt="Merhaba"
txt=txt.join("Dünya")
print(txt)

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)
print(x) 

txt="merhabalar ankaRa"
txt=txt.title()
txt=txt.swapcase()
lw=txt.lower()
up=txt.upper()
# txt=txt.capitalize()

print(txt)
print(lw)
print(up)
