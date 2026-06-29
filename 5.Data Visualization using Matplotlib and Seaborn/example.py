import matplotlib.pyplot as plt

kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
rohit = [0, 0, 0, 1000, 1200, 700, 1900, 1500, 1300, 1900]
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

plt.style.use('seaborn-v0_8-poster')
plt.plot(years, kohli,"go--", label="Virat Kohli")
plt.plot(years, sehwag,'r>:', label="Virender Sehwag")
plt.plot(years, rohit,'b*-.', label="Rohit Sharma")
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.grid(True)
plt.legend()
plt.show()