"""This program reads data from csv files and creates a map with flights from Tallinn."""

import pandas as pd
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def create_data_pre_covid():
    # Import data from files using pandas
    otselennud = pd.read_csv('otselennud.csv', sep=";")
    airports = pd.read_csv('airports.dat', sep=",")

    # Create new data by merging imported data using pandas
    pre_covid = pd.merge(otselennud, airports, on="IATA")

    return pre_covid

def create_data_post_covid():
    # Import data from files using pandas
    airports = pd.read_csv('airports.dat', sep=",")
    flights21 = pd.read_csv('flights21.csv', sep=";")

    # Create new data by merging imported data using pandas
    post_covid = pd.merge(flights21, airports, on="IATA")

    return post_covid


def create_map():
    # Draw map
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Add map features
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)

    ax.set_extent([-20, 50, 25, 70], crs=ccrs.PlateCarree()) # coordinate system specifying the extents


def draw_destinations():
    pre_covid = create_data_pre_covid()
    post_covid = create_data_post_covid()

    tln_lon = 24.832799911499997
    tln_lat = 59.41329956049999

    # Add destination
    for row in pre_covid.itertuples():
        plt.plot([row.Longitude, tln_lon], [row.Latitude, tln_lat],
                 color='green',
                 linewidth=1,
                 marker='o',
                 transform=ccrs.Geodetic())
        plt.text(row.Longitude, row.Latitude, row.IATA,
                 fontsize=6,
                 horizontalalignment='right',
                 transform=ccrs.Geodetic())
        for row2 in post_covid.itertuples():
            plt.plot([row2.Longitude, tln_lon], [row2.Latitude, tln_lat],
                     color='red',
                     linewidth=1,
                     marker='o',
                     transform=ccrs.Geodetic())

    # Create map title
    plt.title('TLN lennud enne ja pärast COVID-it | Johanna Kommer', fontsize=10)

    # Save as png image
    plt.savefig("TLN_map.png")

    plt.show()


if __name__ == '__main__':
    create_data_pre_covid()
    create_data_post_covid()
    create_map()
    draw_destinations()
