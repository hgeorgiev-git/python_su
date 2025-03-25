import matplotlib.pyplot as plt
from astropy import units as u
plt.ion()

b = [28, 45, 80] * u.second
c = [3, 7, 10] * u.meter

plt.figure()

plt.plot(b, c, 'og', ls='')
plt.xlabel('seconds')
plt.ylabel('distance')

plt.savefig('test.png')

print('DONE: figure saved')
