sec =(int(input('Enter the number of second to convert to hh.mm.ss format: ')))
print(f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:.0f}")