a = "Nama saya adalah Al Agias Bayuasa"

cari = ["adw", "Yudha", "Dhema",]

# if cari in a :
#     print("ada")
# else :
#     print("tidak ada")

if any(word in a for word in cari):
    print("ada")
else :
    print("tidak ada")