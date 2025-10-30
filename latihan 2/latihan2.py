

modal_awal = 100000000  
laba = 0

print("Program menghitung total laba selama 8 bulan\n")

for bulan in range(1, 9):
    if bulan in [1, 2]:
        laba_bulan = 0
    elif bulan in [3, 4]:
        laba_bulan = modal_awal * 0.01
    elif bulan in [5, 6, 7]:
        
        laba_bulan = modal_awal * 0.05
    else:
        laba_bulan = modal_awal * 0.03

    print(f"laba bulan ke- {bulan} sebesar: {laba_bulan}")
    laba += laba_bulan

print("\nTotal laba adalah:", laba)