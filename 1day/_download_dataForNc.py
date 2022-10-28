import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': 'total_precipitation',
        'year': '2019',
        'month': '01',
        'time': '00:00',
        'format': 'netcdf',
        'area': [
            45, 0, 43,
            11,
        ],
    },
    'download.nc')