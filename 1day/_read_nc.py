from netCDF4 import Dataset,num2date
nc_file1 = Dataset('download.nc')
print(nc_file1.variables.keys())
print ("longitude_________________")
print(nc_file1.variables['longitude'][:])
print ("latitude_________________")
print(nc_file1.variables['latitude'][:])
print ("time_________________")
print(nc_file1.variables['time'][:])
print ("tp_________________")
print(nc_file1.variables['tp'][:])


